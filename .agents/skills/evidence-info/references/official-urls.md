# Official Reference URLs

Verified canonical URLs for UX audit technical citations.
Agent should verify these are still live before using. If dead, search for replacement.

## Nielsen's 10 Usability Heuristics

Source page: https://www.nngroup.com/articles/ten-usability-heuristics/

| # | Name | Canonical URL | Quote |
|---|------|---------------|-------|
| 1 | Visibility of System Status | https://www.nngroup.com/articles/visibility-system-status/ | "The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time." |
| 2 | Match Between System and Real World | https://www.nngroup.com/articles/match-system-real-world/ | "The design should speak the users' language. Use words, phrases, and concepts familiar to the user." |
| 3 | User Control and Freedom | https://www.nngroup.com/articles/user-control-and-freedom/ | "Users often perform actions by mistake. They need a clearly marked 'emergency exit' to leave the unwanted action." |
| 4 | Consistency and Standards | https://www.nngroup.com/articles/consistency-and-standards/ | "Users should not have to wonder whether different words, situations, or actions mean the same thing." |
| 5 | Error Prevention | https://www.nngroup.com/articles/slips/ | "Good error messages are important, but the best designs carefully prevent problems from occurring in the first place." |
| 6 | Recognition Rather Than Recall | https://www.nngroup.com/articles/recognition-and-recall/ | "Minimize the user's memory load by making elements, actions, and options visible." |
| 7 | Flexibility and Efficiency of Use | https://www.nngroup.com/articles/flexibility-efficiency-heuristic/ | "Shortcuts — hidden from novice users — may speed up the interaction for the expert user." |
| 8 | Aesthetic and Minimalist Design | https://www.nngroup.com/articles/aesthetic-minimalist-design/ | "Interfaces should not contain information that is irrelevant or rarely needed." |
| 9 | Help Users Recognize, Diagnose, and Recover from Errors | https://www.nngroup.com/articles/error-message-guidelines/ | "Error messages should be expressed in plain language, precisely indicate the problem, and constructively suggest a solution." |
| 10 | Help and Documentation | https://www.nngroup.com/articles/help-and-documentation/ | "It's best if the system doesn't need any additional explanation. However, it may be necessary to provide documentation." |

## WCAG 2.2 Success Criteria

Base URL: https://www.w3.org/WAI/WCAG22/Understanding/

| SC | Name | URL | Level |
|----|------|-----|-------|
| 1.4.3 | Contrast (Minimum) | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | AA |
| 1.4.11 | Non-text Contrast | https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html | AA |
| 2.5.5 | Target Size (Enhanced) | https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html | AAA |
| 2.5.8 | Target Size (Minimum) | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | AA |
| 3.3.1 | Error Identification | https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html | A |
| 3.3.2 | Labels or Instructions | https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html | A |
| 3.3.3 | Error Suggestion | https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html | AA |
| 3.3.4 | Error Prevention (Legal, Financial, Data) | https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html | AA |

## Laws of UX

Source: https://lawsofux.com/

| Law | URL | Quote |
|-----|-----|-------|
| Fitts's Law | https://lawsofux.com/fittss-law/ | "The time to acquire a target is a function of the distance to and size of the target." |
| Hick's Law | https://lawsofux.com/hicks-law/ | "The time it takes to make a decision increases with the number and complexity of choices." |
| Jakob's Law | https://lawsofux.com/jakobs-law/ | "Users spend most of their time on other sites. This means that users prefer your site to work the same way." |
| Miller's Law | https://lawsofux.com/millers-law/ | "The average person can only keep 7 (plus or minus 2) items in their working memory." |
| Peak-End Rule | https://lawsofux.com/peak-end-rule/ | "People judge an experience largely based on how they felt at its most intense point and at its end." |
| Zeigarnik Effect | https://lawsofux.com/zeigarnik-effect/ | "People remember uncompleted or interrupted tasks better than completed tasks." |
| Von Restorff Effect | https://lawsofux.com/von-restorff-effect/ | "When multiple similar objects are present, the one that differs from the rest is most likely to be remembered." |
| Doherty Threshold | https://lawsofux.com/doherty-threshold/ | "Productivity soars when a computer and its users interact at a pace (<400ms) that ensures that neither has to wait on the other." |
| Aesthetic-Usability Effect | https://lawsofux.com/aesthetic-usability-effect/ | "Users often perceive aesthetically pleasing design as design that's more usable." |

## Context Mapping Rules

When determining which heuristic/law to cite for a finding:

| Finding Context | Primary Citation | Secondary |
|----------------|-----------------|-----------|
| Missing countdown/timer/status indicator | Nielsen #1 | Zeigarnik Effect |
| Button/CTA inconsistent labeling | Nielsen #4 | Jakob's Law |
| Destructive action without distinction | Nielsen #5 | Von Restorff Effect |
| Missing error message/validation | Nielsen #9 | WCAG 3.3.1 |
| Complex form without guidance | Nielsen #6 | Miller's Law |
| Too many options on screen | Nielsen #8 | Hick's Law |
| Small touch targets | WCAG 2.5.8 | Fitts's Law |
| Poor contrast | WCAG 1.4.3 | — |
| Missing undo/back/cancel | Nielsen #3 | — |
| Content not matching user mental model | Nielsen #2 | Jakob's Law |
| Empty state without guidance | Nielsen #6 | — |
| Repeated/redundant content | Nielsen #8 | — |
| Financial/legal action without confirmation | WCAG 3.3.4 | Nielsen #5 |
