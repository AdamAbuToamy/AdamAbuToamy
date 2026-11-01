# Media provenance and capture notes

Audit and captures: 1 November 2026. Only the profile repository was changed.

## WILO

The `wilo-*.png` files are direct Playwright/Chrome screenshots of https://where-i-left-off.web.app/ with fictional demo content. Screenshots use element capture or an explicit crop; account identity is excluded. No DOM, HTML, authorization rules or production code was modified to manufacture a screen.

`wilo-showcase.mp4` is a newly edited 32.5-second H.264, 1920×1080 film. It combines an actual Playwright screen recording and direct screenshots with original title graphics and crossfades. Screenshots are still captures, not represented as continuous interaction. The screen recording is cropped to exclude the identity row. There is no audio or music. `wilo-preview.gif` is a six-second, 640-pixel-wide derivative; `wilo-video-cover.png` is the title frame.

Captured journeys: five personal cards created through the UI, two personal sections, card editing and next-step saving, checklist progress, Cards/Week navigation, manual session notes, session checklist, and a 390×844 viewport. Card persistence was verified after reloading. A checked session item and a manual note reached the actual Saved state.

The test account was verified against the signed-in Firebase account email in memory. Seven pre-existing personal cards were matched to the personal account-scoped local store, backed up as JSON plus a UI-exported PDF outside Git and publication directories, and moved to the app's recoverable Trash through the UI. Reload confirmed zero active cards before demo creation. No shared data, courses or account configuration were deleted. Backup files, session state, raw recordings and account identifiers are not published.

University returned “Verify your account email to open University.” The account email is unverified. The AI widget is unavailable to this account; no AI execution or review/apply success was captured. No email-verification bypass was attempted. Cloud voice recognition was not tested and is not presented as successful. The university/AI storyboard scenes were replaced with demonstrated cards and sessions.

Initial headless Chrome received App Check HTTP 403 and failed account reads. A regular headed Chrome Playwright session succeeded without bypassing verification or changing site security. This is a capture-environment observation, not evidence that all environments work.

The project's existing `docs/media/images` and `docs/media/videos` are promotional illustrations / animated recreations according to its own media README. None was substituted for a live UI screenshot.

## Robot Arm Studio

- Source: [docs/media/VID-20261010-WA0009.mp4](https://github.com/AdamAbuToamy/RobotArmStudio/blob/main/docs/media/VID-20261010-WA0009.mp4), 480×860, 14.527 seconds, original physical build recording.
- `robot-arm.jpg`: frame at approximately 9 seconds; actual arm and build bench.
- `robot-motion.gif`: approximately seconds 8–12, 320 pixels wide, 8 fps, 64-color palette. Genuine recorded movement, not animation generated from a still.
- Legacy names `robot-and-controller.jpg`, `robot-control.gif`, `robot-control-demo.mp4` and `robot-motion-demo.mp4` are absent from current source main. They were removed from the profile links.
- Mechanical design credit: [FABRI_CREATOR](https://cults3d.com/en/3d-model/gadget/brazo-robotico-con-arduino-step-files-robotic-arm-guardar-reproducir-export). No purchased CAD/STL is redistributed. See the source repository's [attribution](https://github.com/AdamAbuToamy/RobotArmStudio/blob/main/ATTRIBUTION.md).

## FPV Drone

- `drone-build.jpg`: resized/recompressed derivative of [docs/media/20260903_023031.jpg](https://github.com/AdamAbuToamy/FPV-Drone/blob/main/docs/media/20260903_023031.jpg), an original build/soldering photograph. Original dimensions 4000×3000; orientation handled by the existing source pixels.
- Six original photographs were inventoried; source images were not edited in their repository.
- Legacy names `drone-built.jpg`, `drone-bench-demo.mp4` and `betaflight-orientation-demo.mp4` are absent from current source main.
- Direct checks of three original video attachment URLs returned HTTP 404. Their asset IDs were `339ed626-3194-44b6-aee0-c97dae2871ad`, `21cfbd32-adca-454b-84b0-b1329708a2ee` and `42ae3da9-a804-4ace-8616-e8e0ee8b7744`. No drone GIF was fabricated from photos or unrelated footage.

## DeskPages

- Original [Concept Promo](https://github.com/user-attachments/assets/1604baac-4e1b-4fa8-92d0-7a5c943df32d) downloaded successfully. Its bytes match the repository's `media/DeskPages-demo.mp4`: 10.01 seconds, 720×1280, H.264/AAC. The source README explicitly calls it an **AI-generated concept visualization**.
- `deskpages-concept.gif`: silent six-second excerpt, approximately seconds 2–8, 270 pixels wide, 10 fps. It is labelled Concept Promo in the profile and links to the full original. No large duplicate video is added.
- `deskpages-tour.gif`: unchanged from `media/DeskPages-tour-0.8.9-en.gif`. Actual app UI captured with test data under Mono/Xvfb; source caveat about Windows fonts/borders retained.
- `deskpages-settings.png`: unchanged from `media/DeskPages-settings-0.8.12-en.png`, with the same environment caveat.

## Technology evidence

- WILO `package.json`, `src/lib/firebase.ts`, `push-worker/`: React, TypeScript, JavaScript, Firebase Authentication, Firestore, Vite, Vitest, Playwright, Cloudflare Workers. Source contains HTML/CSS and worker SQLite/D1 work.
- Robot Arm Studio `requirements.txt`, controller/firmware documentation: Python, aiohttp, ESP32-S3, PCA9685 and servos.
- DeskPages `Agent.ps1`, `Installer/`, `Interaction/`, third-party notices: PowerShell, C#, .NET/WinForms and native Windows integrations. WPF was removed from the previous profile because current source evidence here is WinForms.
- STOMP Emergency README, server/client sources, workflow and dashboard: Java, C++, TCP, STOMP, TPC/Reactor, Python, SQLite, Linux/WSL, Maven, GitHub Actions.
- Kanban Backend README and `KanbanApp/Kanban_BackEnd`: C#/.NET, Service/Business layers and backend tests.

No project test suite was rerun for this media/README change; historical project test results are not presented as fresh results. Ammar Mawassi's original STOMP collaboration credit is retained. Profile design SVGs and title backgrounds are original decorative assets, not project screenshots.
