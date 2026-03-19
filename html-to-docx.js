#!/usr/bin/env node
/**
 * html-to-docx.js v2 — Convert UX Audit Pitch Deck HTML to Word Document
 * 
 * FIXED: Google Docs compatibility
 * - Uses DXA (twips) instead of PERCENTAGE for table widths
 * - Avoids nested tables that Google Docs can't render
 * - Correct aspect ratio for images
 * - Simplified layout for maximum compatibility
 * 
 * Usage: node html-to-docx.js <path-to-pitch-deck.html> [output.docx]
 */

const fs = require('fs');
const path = require('path');
const { load } = require('cheerio');
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  ImageRun,
  Table,
  TableRow,
  TableCell,
  WidthType,
  AlignmentType,
  BorderStyle,
  ShadingType,
  VerticalAlign,
  TableLayoutType,
  convertInchesToTwip,
} = require('docx');

// Page layout: A4 with 0.8in margins → content width ≈ 6.7in = 9648 twips
const PAGE_WIDTH_TWIPS = convertInchesToTwip(6.7);
const COL_IMG_TWIPS = convertInchesToTwip(2.4);   // ~36% for image column
const COL_CONTENT_TWIPS = PAGE_WIDTH_TWIPS - COL_IMG_TWIPS; // ~64% for content

// ─── Color tokens ───
const C = {
  gold: 'D97706',
  purple: '7C3AED',
  blue: '2563EB',
  critical: 'DC2626',
  criticalBg: 'FEE2E2',
  criticalText: 'B91C1C',
  major: 'EA580C',
  majorBg: 'FFF7ED',
  majorText: 'C2410C',
  minor: 'CA8A04',
  minorBg: 'FEF9C3',
  minorText: 'A16207',
  pass: '16A34A',
  passBg: 'DCFCE7',
  dark: '111827',
  darkGray: '374151',
  medGray: '6B7280',
  lightGray: '9CA3AF',
  divider: 'D1D5DB',
  cardBg: 'F9FAFB',
  headerBg: 'F3F4F6',
  white: 'FFFFFF',
};

const SEV = {
  critical: { color: C.critical, bg: C.criticalBg, text: C.criticalText, label: 'CRITICAL' },
  major: { color: C.major, bg: C.majorBg, text: C.majorText, label: 'MAJOR' },
  minor: { color: C.minor, bg: C.minorBg, text: C.minorText, label: 'MINOR' },
};

// ─── Helpers ───
function getImageBuffer(htmlDir, src) {
  const p = path.resolve(htmlDir, src);
  return fs.existsSync(p) ? fs.readFileSync(p) : null;
}

function getPngDimensions(buf) {
  if (!buf || buf.length < 24 || buf[0] !== 0x89 || buf[1] !== 0x50) return null;
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
}

function cleanText(text) {
  return (text || '')
    .replace(/\s+/g, ' ')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ')
    .trim();
}

function noBorder() {
  return {
    top: { style: BorderStyle.NONE, size: 0 },
    bottom: { style: BorderStyle.NONE, size: 0 },
    left: { style: BorderStyle.NONE, size: 0 },
    right: { style: BorderStyle.NONE, size: 0 },
  };
}

function thinBorder(color = C.divider) {
  const b = { style: BorderStyle.SINGLE, size: 1, color };
  return { top: b, bottom: b, left: b, right: b };
}

function spacer(pts = 12) {
  return new Paragraph({ spacing: { before: pts * 20, after: pts * 20 } });
}

function divider() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: C.divider } },
  });
}

function sectionNum(num, label) {
  return new Paragraph({
    spacing: { before: 400, after: 60 },
    children: [
      new TextRun({ text: `${num}  `, font: 'Calibri', size: 20, color: C.gold, bold: true }),
      new TextRun({ text: label, font: 'Calibri', size: 20, color: C.gold, bold: true }),
    ],
  });
}

function sectionTitle(text) {
  return new Paragraph({
    spacing: { after: 200 },
    children: [
      new TextRun({ text, font: 'Calibri', size: 36, bold: true, color: C.dark }),
    ],
  });
}

function sectionDesc(text) {
  return new Paragraph({
    spacing: { after: 240 },
    children: [
      new TextRun({ text, font: 'Calibri', size: 21, color: C.medGray }),
    ],
  });
}

// ─── Parse HTML ───
function parseHtml(htmlPath) {
  const $ = load(fs.readFileSync(htmlPath, 'utf-8'));
  const htmlDir = path.dirname(htmlPath);
  const data = { title: '', subtitle: '', stats: [], methods: [], findings: [], scores: [], actionRows: [], footer: '' };

  data.title = cleanText($('.hero h1').text());
  data.subtitle = cleanText($('.hero .subtitle').text());

  $('.stat-card').each((_, el) => {
    data.stats.push({
      value: cleanText($(el).find('.stat-value').attr('data-target') || $(el).find('.stat-value').text()),
      label: cleanText($(el).find('.stat-label').text()),
      type: $(el).find('.stat-value').hasClass('score') ? 'score'
        : $(el).find('.stat-value').hasClass('screens') ? 'screens'
          : $(el).find('.stat-value').hasClass('checks') ? 'checks' : 'findings',
    });
  });

  $('.method-card').each((_, el) => {
    data.methods.push({
      icon: cleanText($(el).find('.method-icon').text()),
      title: cleanText($(el).find('h3').text()),
      desc: cleanText($(el).find('p').text()),
    });
  });

  $('.finding-card').each((_, el) => {
    const $el = $(el);
    const severity = $el.find('.finding-accent').hasClass('critical') ? 'critical'
      : $el.find('.finding-accent').hasClass('major') ? 'major' : 'minor';
    const imgSrc = $el.find('.phone-frame img').attr('src') || '';
    const imgBuf = getImageBuffer(htmlDir, imgSrc);

    const sections = [];
    $el.find('.card-info .finding-section').each((_, sec) => {
      const $sec = $(sec);
      const title = cleanText($sec.find('h4').text());
      const $box = $sec.find('.proposed-box');
      if ($box.length) {
        const items = [];
        $box.find('li').each((_, li) => items.push(cleanText($(li).text())));
        sections.push({ title, isProposal: true, proposedTitle: cleanText($box.find('h5').text()), items });
      } else {
        const items = [];
        $sec.find('li').each((_, li) => items.push(cleanText($(li).text())));
        sections.push({ title, text: cleanText($sec.find('p').text()), items, isProposal: false });
      }
    });

    const tags = [];
    $el.find('.card-tag').each((_, t) => tags.push(cleanText($(t).text())));

    data.findings.push({
      id: cleanText($el.find('.card-id').text()),
      severity,
      title: cleanText($el.find('.card-info h3').text()),
      imgBuf,
      imgDims: imgBuf ? getPngDimensions(imgBuf) : null,
      caption: cleanText($el.find('.shot-overlay').text()),
      sections,
      tags,
      techRef: cleanText($el.find('.detail-content').text()),
    });
  });

  $('.score-card').each((_, el) => {
    data.scores.push({
      score: parseInt(cleanText($(el).find('.score-label').text())) || 0,
      title: cleanText($(el).find('.score-title').text()),
      detail: cleanText($(el).find('.score-detail').text()),
    });
  });

  let curSprint = '';
  $('.sprint-table tbody tr').each((_, row) => {
    const cells = [];
    $(row).find('td').each((_, c) => {
      cells.push({ text: cleanText($(c).text()), rowspan: parseInt($(c).attr('rowspan') || '1') });
    });
    if (cells.length >= 5) {
      curSprint = cleanText($(row).find('td:first-child strong').text());
      const week = cleanText($(row).find('td:first-child span').text());
      data.actionRows.push({ sprint: `${curSprint} (${week})`, id: cells[1].text, issue: cells[2].text, severity: cells[3].text.toLowerCase().trim(), effort: cells[4].text, isStart: true, rowspan: cells[0].rowspan });
    } else if (cells.length >= 4) {
      data.actionRows.push({ sprint: curSprint, id: cells[0].text, issue: cells[1].text, severity: cells[2].text.toLowerCase().trim(), effort: cells[3].text, isStart: false });
    }
  });

  data.footer = cleanText($('footer p').text());
  return data;
}

// ─── Build Document ───
function buildDoc(data) {
  const c = []; // children array

  // ═══ 1. EXECUTIVE SUMMARY ═══
  c.push(spacer(40));
  c.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 100 },
    children: [new TextRun({ text: 'UX AUDIT REPORT', font: 'Calibri', size: 22, color: C.purple, bold: true })],
  }));
  c.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
    children: [new TextRun({ text: data.title, font: 'Calibri', size: 52, bold: true, color: C.dark })],
  }));
  c.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 360 },
    children: [new TextRun({ text: data.subtitle, font: 'Calibri', size: 22, color: C.medGray, italics: true })],
  }));

  // Stats as 4-column table (DXA widths)
  if (data.stats.length > 0) {
    const typeColor = { score: C.gold, screens: C.blue, checks: C.purple, findings: C.critical };
    const colW = Math.floor(PAGE_WIDTH_TWIPS / data.stats.length);

    c.push(new Table({
      width: { size: PAGE_WIDTH_TWIPS, type: WidthType.DXA },
      rows: [new TableRow({
        children: data.stats.map(s => new TableCell({
          width: { size: colW, type: WidthType.DXA },
          verticalAlign: VerticalAlign.CENTER,
          shading: { type: ShadingType.SOLID, fill: C.cardBg, color: C.cardBg },
          borders: {
            top: { style: BorderStyle.NONE, size: 0 },
            bottom: { style: BorderStyle.SINGLE, size: 4, color: typeColor[s.type] || C.gold },
            left: { style: BorderStyle.SINGLE, size: 1, color: C.white },
            right: { style: BorderStyle.SINGLE, size: 1, color: C.white },
          },
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 160, after: 40 },
              children: [new TextRun({
                text: s.label.toUpperCase() === 'UX SCORE' ? `${s.value}%` : s.value,
                font: 'Calibri', size: 44, bold: true, color: typeColor[s.type] || C.dark,
              })],
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { after: 160 },
              children: [new TextRun({
                text: s.label.toUpperCase(), font: 'Calibri', size: 16, color: C.medGray,
              })],
            }),
          ],
        })),
      })],
    }));
  }

  c.push(spacer(16));
  c.push(divider());

  // ═══ 2. METHODOLOGY ═══
  c.push(sectionNum('02', 'PHƯƠNG PHÁP ĐÁNH GIÁ'));
  c.push(sectionTitle('Phương pháp đánh giá'));

  // Methods: each as a simple bordered paragraph block (no nested tables)
  for (const m of data.methods) {
    c.push(new Paragraph({
      spacing: { before: 120, after: 40 },
      shading: { type: ShadingType.SOLID, fill: C.cardBg, color: C.cardBg },
      border: {
        top: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
        bottom: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
        left: { style: BorderStyle.SINGLE, size: 3, color: C.gold },
        right: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
      },
      children: [
        new TextRun({ text: `${m.icon}  `, font: 'Calibri', size: 24 }),
        new TextRun({ text: m.title, font: 'Calibri', size: 22, bold: true, color: C.dark }),
      ],
    }));
    c.push(new Paragraph({
      spacing: { after: 160 },
      indent: { left: convertInchesToTwip(0.2) },
      children: [new TextRun({ text: m.desc, font: 'Calibri', size: 19, color: C.medGray })],
    }));
  }

  c.push(spacer(8));
  c.push(divider());

  // ═══ 3. DETAILED FINDINGS ═══
  c.push(sectionNum('03', 'CHI TIẾT PHÁT HIỆN'));
  c.push(sectionTitle('Chi tiết phát hiện'));
  c.push(sectionDesc(`${data.findings.length} vấn đề được xác định, sắp xếp theo mức độ ảnh hưởng`));

  for (const f of data.findings) {
    const sev = SEV[f.severity] || SEV.minor;

    // ── Accent top border ──
    c.push(new Paragraph({
      spacing: { before: 300, after: 0 },
      border: { top: { style: BorderStyle.SINGLE, size: 8, color: sev.color } },
    }));

    // ── ID + Badge ──
    c.push(new Paragraph({
      spacing: { before: 80, after: 80 },
      children: [
        new TextRun({ text: f.id, font: 'Consolas', size: 18, color: C.medGray }),
        new TextRun({ text: '   ', font: 'Calibri', size: 18 }),
        new TextRun({
          text: ` ${sev.label} `,
          font: 'Calibri', size: 16, bold: true,
          color: sev.text,
          shading: { type: ShadingType.SOLID, fill: sev.bg, color: sev.bg },
        }),
      ],
    }));

    // ── Title ──
    c.push(new Paragraph({
      spacing: { after: 160 },
      children: [new TextRun({ text: f.title, font: 'Calibri', size: 24, bold: true, color: C.dark })],
    }));

    // ── Image (centered, standalone, BEFORE content) ──
    if (f.imgBuf) {
      const dims = f.imgDims || { width: 375, height: 812 };
      const imgDisplayW = 150; // pixels in docx
      const imgDisplayH = Math.round(imgDisplayW * (dims.height / dims.width));

      c.push(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 80, after: 40 },
        children: [
          new ImageRun({
            data: f.imgBuf,
            transformation: { width: imgDisplayW, height: imgDisplayH },
            type: 'png',
          }),
        ],
      }));

      if (f.caption) {
        c.push(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { after: 160 },
          children: [new TextRun({ text: f.caption, font: 'Calibri', size: 16, color: C.medGray, italics: true })],
        }));
      }
    }

    // ── Sections content ──
    for (const sec of f.sections) {
      // Section header
      c.push(new Paragraph({
        spacing: { before: 120, after: 60 },
        children: [new TextRun({
          text: sec.title.toUpperCase(),
          font: 'Calibri', size: 16, bold: true,
          color: sec.isProposal ? C.pass : C.gold,
        })],
      }));

      if (sec.isProposal) {
        // Green left-border proposed box
        c.push(new Paragraph({
          spacing: { before: 40, after: 40 },
          indent: { left: convertInchesToTwip(0.15) },
          border: { left: { style: BorderStyle.SINGLE, size: 4, color: C.pass } },
          shading: { type: ShadingType.SOLID, fill: C.passBg, color: C.passBg },
          children: [new TextRun({
            text: `✅ ${sec.proposedTitle}`,
            font: 'Calibri', size: 20, bold: true, color: C.pass,
          })],
        }));
        for (const item of sec.items) {
          c.push(new Paragraph({
            spacing: { before: 20, after: 20 },
            indent: { left: convertInchesToTwip(0.3) },
            border: { left: { style: BorderStyle.SINGLE, size: 4, color: C.pass } },
            shading: { type: ShadingType.SOLID, fill: C.passBg, color: C.passBg },
            children: [new TextRun({ text: `• ${item}`, font: 'Calibri', size: 19, color: C.darkGray })],
          }));
        }
      } else if (sec.items?.length > 0) {
        for (const item of sec.items) {
          c.push(new Paragraph({
            spacing: { before: 20, after: 20 },
            indent: { left: convertInchesToTwip(0.2) },
            children: [new TextRun({ text: `• ${item}`, font: 'Calibri', size: 19, color: C.darkGray })],
          }));
        }
      } else if (sec.text) {
        c.push(new Paragraph({
          spacing: { before: 20, after: 60 },
          children: [new TextRun({ text: sec.text, font: 'Calibri', size: 19, color: C.darkGray })],
        }));
      }
    }

    // ── Tags ──
    if (f.tags.length > 0) {
      c.push(new Paragraph({
        spacing: { before: 100, after: 40 },
        children: f.tags.map((t, i) => new TextRun({
          text: `${i > 0 ? '   ' : ''}#${t}`,
          font: 'Calibri', size: 17, color: C.blue,
        })),
      }));
    }

    // ── Tech reference ──
    if (f.techRef) {
      c.push(new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [
          new TextRun({ text: 'Tham chiếu: ', font: 'Calibri', size: 17, color: C.purple, bold: true }),
          new TextRun({ text: f.techRef, font: 'Calibri', size: 17, color: C.medGray, italics: true }),
        ],
      }));
    }

    c.push(spacer(4));
  }

  c.push(divider());

  // ═══ 4. HEURISTIC SCORECARD ═══
  c.push(sectionNum('04', 'HEURISTIC SCORECARD'));
  c.push(sectionTitle('Heuristic Scorecard'));

  if (data.scores.length > 0) {
    const colW = Math.floor(PAGE_WIDTH_TWIPS / data.scores.length);
    const scoreColor = s => s >= 80 ? C.pass : s >= 70 ? C.gold : s >= 60 ? C.major : C.critical;

    c.push(new Table({
      width: { size: PAGE_WIDTH_TWIPS, type: WidthType.DXA },
      rows: [new TableRow({
        children: data.scores.map(s => new TableCell({
          width: { size: colW, type: WidthType.DXA },
          verticalAlign: VerticalAlign.CENTER,
          shading: { type: ShadingType.SOLID, fill: C.cardBg, color: C.cardBg },
          borders: {
            top: { style: BorderStyle.SINGLE, size: 4, color: scoreColor(s.score) },
            bottom: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
            left: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
            right: { style: BorderStyle.SINGLE, size: 1, color: C.divider },
          },
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 200, after: 40 },
              children: [new TextRun({
                text: `${s.score}%`, font: 'Consolas', size: 40, bold: true, color: scoreColor(s.score),
              })],
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { after: 40 },
              children: [new TextRun({ text: s.title, font: 'Calibri', size: 20, color: C.darkGray })],
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { after: 160 },
              children: [new TextRun({ text: s.detail, font: 'Calibri', size: 16, color: C.lightGray })],
            }),
          ],
        })),
      })],
    }));
  }

  c.push(spacer(16));
  c.push(divider());

  // ═══ 5. ACTION PLAN ═══
  c.push(sectionNum('05', 'KẾ HOẠCH HÀNH ĐỘNG'));
  c.push(sectionTitle('Kế hoạch hành động'));

  if (data.actionRows.length > 0) {
    // Column widths in DXA (Sprint:2in, ID:0.8in, Issue:2.4in, Severity:0.8in, Effort:0.7in)
    const colWidths = [
      convertInchesToTwip(1.8),
      convertInchesToTwip(0.8),
      convertInchesToTwip(2.4),
      convertInchesToTwip(0.9),
      convertInchesToTwip(0.7),
    ];

    const headerTexts = ['Sprint', 'ID', 'Vấn đề', 'Mức độ', 'Effort'];
    const headerRow = new TableRow({
      children: headerTexts.map((h, i) => new TableCell({
        width: { size: colWidths[i], type: WidthType.DXA },
        shading: { type: ShadingType.SOLID, fill: C.dark, color: C.dark },
        borders: noBorder(),
        children: [new Paragraph({
          spacing: { before: 80, after: 80 },
          children: [new TextRun({ text: h.toUpperCase(), font: 'Calibri', size: 16, bold: true, color: C.white })],
        })],
      })),
    });

    const rows = [headerRow];

    // Group by sprint
    const groups = {};
    const groupOrder = [];
    for (const r of data.actionRows) {
      if (!groups[r.sprint]) {
        groups[r.sprint] = [];
        groupOrder.push(r.sprint);
      }
      groups[r.sprint].push(r);
    }

    let rowIdx = 0;
    for (const sprint of groupOrder) {
      const items = groups[sprint];
      for (let i = 0; i < items.length; i++) {
        const r = items[i];
        const bg = rowIdx % 2 === 0 ? C.white : C.cardBg;
        const bdr = thinBorder(C.divider);
        const sevKey = r.severity.replace(/\s/g, '');
        const sev = SEV[sevKey] || SEV.minor;

        const cells = [];

        // Sprint cell (merged rows)
        if (i === 0) {
          cells.push(new TableCell({
            width: { size: colWidths[0], type: WidthType.DXA },
            rowSpan: items.length,
            verticalAlign: VerticalAlign.CENTER,
            shading: { type: ShadingType.SOLID, fill: bg, color: bg },
            borders: bdr,
            children: [new Paragraph({
              spacing: { before: 60, after: 60 },
              children: [new TextRun({ text: sprint, font: 'Calibri', size: 19, bold: true, color: C.dark })],
            })],
          }));
        }

        // ID
        cells.push(new TableCell({
          width: { size: colWidths[1], type: WidthType.DXA },
          shading: { type: ShadingType.SOLID, fill: bg, color: bg },
          borders: bdr, verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            spacing: { before: 60, after: 60 },
            children: [new TextRun({ text: r.id, font: 'Consolas', size: 17, color: C.medGray })],
          })],
        }));

        // Issue
        cells.push(new TableCell({
          width: { size: colWidths[2], type: WidthType.DXA },
          shading: { type: ShadingType.SOLID, fill: bg, color: bg },
          borders: bdr, verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            spacing: { before: 60, after: 60 },
            children: [new TextRun({ text: r.issue, font: 'Calibri', size: 19, color: C.darkGray })],
          })],
        }));

        // Severity
        cells.push(new TableCell({
          width: { size: colWidths[3], type: WidthType.DXA },
          shading: { type: ShadingType.SOLID, fill: bg, color: bg },
          borders: bdr, verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 60, after: 60 },
            children: [new TextRun({
              text: ` ${sev.label} `,
              font: 'Calibri', size: 15, bold: true, color: sev.text,
              shading: { type: ShadingType.SOLID, fill: sev.bg, color: sev.bg },
            })],
          })],
        }));

        // Effort
        cells.push(new TableCell({
          width: { size: colWidths[4], type: WidthType.DXA },
          shading: { type: ShadingType.SOLID, fill: bg, color: bg },
          borders: bdr, verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            spacing: { before: 60, after: 60 },
            children: [new TextRun({ text: r.effort, font: 'Calibri', size: 19, bold: true, color: C.dark })],
          })],
        }));

        rows.push(new TableRow({ children: cells }));
        rowIdx++;
      }
    }

    c.push(new Table({
      width: { size: PAGE_WIDTH_TWIPS, type: WidthType.DXA },
      layout: TableLayoutType.FIXED,
      rows,
    }));
  }

  // Footer
  c.push(spacer(24));
  c.push(divider());
  c.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 160, after: 160 },
    children: [new TextRun({
      text: data.footer || 'Co-opBank KHCN · Powered by Design Data Layer',
      font: 'Calibri', size: 18, color: C.lightGray, italics: true,
    })],
  }));

  return new Document({
    styles: {
      default: {
        document: { run: { font: 'Calibri', size: 22 } },
      },
    },
    sections: [{
      properties: {
        page: {
          margin: {
            top: convertInchesToTwip(0.8),
            right: convertInchesToTwip(0.8),
            bottom: convertInchesToTwip(0.8),
            left: convertInchesToTwip(0.8),
          },
        },
      },
      children: c,
    }],
  });
}

// ─── Main ───
async function main() {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.error('Usage: node html-to-docx.js <pitch-deck.html> [output.docx]');
    process.exit(1);
  }

  const htmlPath = path.resolve(args[0]);
  if (!fs.existsSync(htmlPath)) {
    console.error(`❌ File not found: ${htmlPath}`);
    process.exit(1);
  }

  const outPath = args[1]
    ? path.resolve(args[1])
    : path.join(path.dirname(htmlPath), `${path.basename(htmlPath, '.html')}.docx`);

  console.log(`📄 Input:  ${htmlPath}`);
  console.log(`📁 Output: ${outPath}`);
  console.log('─'.repeat(50));

  console.log('🔍 Parsing HTML...');
  const data = parseHtml(htmlPath);
  console.log(`   Title: ${data.title}`);
  console.log(`   Stats: ${data.stats.length} | Methods: ${data.methods.length}`);
  console.log(`   Findings: ${data.findings.length} | Scores: ${data.scores.length}`);
  console.log(`   Actions: ${data.actionRows.length}`);
  console.log(`   Images: ${data.findings.filter(f => f.imgBuf).length}/${data.findings.length}`);

  console.log('📝 Building document...');
  const doc = buildDoc(data);

  console.log('📦 Packing .docx...');
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(outPath, buf);

  console.log('─'.repeat(50));
  console.log(`✅ Done! ${outPath} (${(buf.length / 1024).toFixed(0)} KB)`);
}

main().catch(err => {
  console.error('❌ Error:', err.message);
  process.exit(1);
});
