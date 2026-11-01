# Profile presentation QA — 1 November 2026

Checked on the published `showcase/real-engineering-2026-11` branch using the actual GitHub-rendered README before main publication.

- Desktop: 1440×1000 viewport, 838-pixel README content area; all images loaded. Full-page capture and visual review covered hero, WILO, hardware, DeskPages, software, stack, current work and contact.
- Mobile: 390×844 viewport, 324-pixel README content area; the browser selected `hero-mobile.svg`. All images loaded; no document horizontal overflow. Technology badges wrapped within the content width.
- Light and dark GitHub backgrounds checked; dark body background was RGB(13,17,23). Hero text is legible with no overlapping or truncated text in its source bounds.
- Seven section headers have narrower SVG variants. No custom CSS, JavaScript, iframe or HTML video element is used in the README.
- WILO precedes DeskPages. Real robot photo/motion and drone build photograph rendered successfully. DeskPages concept preview occupies 26% of the content width alongside its actual UI tour.
- Local reference check: 91 references, zero missing relative targets, no test-account identifiers or credential markers in README/provenance text.
- HTTP checks: 66 unique rendered links/assets checked. The DeskPages attachment rejects HEAD but succeeds with GET and serves `video/mp4`. The original Cults3D credit page returned HTTP 403 to automated requests; the designer credit is independently preserved in the project's GitHub attribution document. No claim is made that this protected page passed the automated check.
- The WILO MP4 decodes completely; H.264, 1920×1080, 32.5 seconds, no audio. Approximately 1.6 MB. Its GIF preview is approximately 323 KB. Robot GIF approximately 2 MB; DeskPages concept GIF approximately 1.5 MB. No large source recording is copied into the profile.
- WILO direct captures were visually inspected for actual UI content and privacy. Five demo cards persisted across reload. Manual session note and checked session checklist item reached Saved. No shared records or courses were modified.

Limits: University/AI execution requires verified account email and was unavailable to the test account. Voice recognition and physical-device behavior were not tested. Drone video derivatives were omitted because checked original attachment links returned 404. Project test suites were not rerun for this presentation-only change.

Final main/profile screenshots are delivered separately after merge; this file records the pre-merge gate, not a substitute for the post-publication check.
