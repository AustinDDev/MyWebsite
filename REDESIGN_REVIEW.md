# Portfolio redesign review

## Phase 1 — audit and direction
The starting branch was redesign/christopher-style at f34404e. It contained five static HTML pages, corrected professional copy, a printer case study, six planned project entries, a resume PDF, and an academic capstone PDF. All are retained. The old main.js referenced nonexistent theme controls and was unused. The starting stylesheet used cream surfaces contrary to the brief. Homepage content repeated several themes and the academic projects had no dedicated case studies.

Direction: matte black and charcoal, forest-green actions, restrained editorial typography, generous spacing, and original CSS/SVG infrastructure graphics. System typography removes external font requests. No framework or package dependencies were added. The inspiration URL could not be accessed; this is an original interpretation of the written direction.

## Implementation
- Shared sticky navigation, footer, active-page states, dark palette, responsive grids, focus styles, skip links, and reduced-motion support.
- New homepage hero and conceptual network illustration; visual panels for three featured case studies.
- Existing About, Projects, Contact, printer case study, URLs, PDFs, and six planned project descriptions retained.
- Added network-design-case-study.html and security-culture-case-study.html. Shared case-study CSS supports role, challenge, architecture, technologies, implementation, security, evidence, testing, results, and lessons. Academic limitations remain explicit.
- Printer diagram separates network-only DCA monitoring from Excel page-count tracking. No automatic integration, ink-consumption measurement, or savings is claimed.
- Removed public HTML team and domain counts as an additional privacy measure.

## Privacy history finding
Earlier public Git history contains employer workforce and device inventory figures. Confirmed affected commits include 57f0771, 9a92a4a, 0b1c286, 45e2fa7, ceb03cf, and d8ebffb. The repository log also records later removal commits, including f34404e. No sensitive figures are repeated here. Review the affected HTML and PORTFOLIO_COPY.md versions in a private setting. This audit covers the cloned development branch history, not every remote ref, fork, cache, or attachment.

Deleting figures from current pages does not remove earlier public commits. Privately assess the disclosure with the appropriate information owner. If removal is required, plan a coordinated history cleanup using GitHub's documented sensitive-data process, including affected refs, forks, cached views, and collaborator clones. Rewriting history requires separate approval; no history was rewritten. There is no evidence from this review that credentials were involved.

## Content review needed before launch
The preserved resume PDF is outdated: it omits current IT roles, describes the cybersecurity degree as in progress, and contains older education/date and project-deployment wording. A visible notice appears on Contact. Replace it with a reviewed, current resume before publication. The academic capstone PDF uses simulated implementation language; the new case study explicitly identifies it as an academic proposal. The security research paper is absent, so the page transparently provides only a summary. No new certifications or metrics were added.

## Validation
Seven pages and 107 link references passed static local-file/anchor checks. Each page has one h1 and unique IDs. Main palette text combinations tested at 17.57:1, 8.53:1, 5.51:1 and 4.73:1 (see validation.json). No external fonts or runtime dependencies are requested. Responsive breakpoints support phone, tablet, and desktop; browser rendering, keyboard interaction, and performance measurements remain unverified.

The local Python preview could not be reached through the in-app browser. A replacement Node preview started successfully, but the browser returned a session ownership error. A native preview-opening request was queued. This is not a passed browser test, and no screenshots are represented as verified.

## Review locally
Extract portfolio-redesign.zip. From the extracted directory run `python -m http.server 4173`, then open http://localhost:4173 in a browser. Inspect at 390px, 768px and 1440px widths; check navigation, keyboard focus, all case studies, PDF links, and reduced-motion preferences.

Changes are saved locally on redesign/christopher-style. Nothing was pushed, merged into main, or published. Approval is required before merging or publishing, as requested.
