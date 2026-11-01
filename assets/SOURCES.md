# Media provenance and capture notes

Audit and captures: 1 November 2026. Only the profile repository was changed.

## WILO

The `wilo-*.png` files are direct Playwright/Chrome screenshots of https://where-i-left-off.web.app/ with fictional demo content. Screenshots use element capture or an explicit crop; account identity is excluded. No DOM, HTML, authorization rules or production code was modified to manufacture a screen.

`wilo-showcase.mp4` was rebuilt for clarity as a 34-second H.264, 1920×1080 film. Fresh direct Playwright screenshots use 2× device pixel density, with larger UI panels, camera pans over real still captures and original title graphics/crossfades. Still captures are not represented as continuous screen interaction. Identity is excluded through direct element capture or cropping. There is no audio or music. The master uses CRF 16 after lossless intermediate segments. `wilo-preview.gif` is a five-second, 960-pixel-wide derivative with a 128-color palette. `wilo-video-cover.png` is a full-resolution frame from the film.

Captured journeys: five personal cards created through the UI, two personal sections, card editing and next-step saving, checklist progress, Cards/Week navigation, manual session notes, session checklist, and a 390×844 viewport. Card persistence was verified after reloading. A checked session item and a manual note reached the actual Saved state.

The test account was verified against the signed-in Firebase account email in memory. Seven pre-existing personal cards were matched to the personal account-scoped local store, backed up as JSON plus a UI-exported PDF outside Git and publication directories, and moved to the app's recoverable Trash through the UI. Reload confirmed zero active cards before demo creation. No shared data, courses or account configuration were deleted. Backup files, session state, raw recordings and account identifiers are not published.

University returned “Verify your account email to open University.” The account email is unverified. The AI widget is unavailable to this account; no AI execution or review/apply success was captured. No email-verification bypass was attempted. Cloud voice recognition was not tested and is not presented as successful. The university/AI storyboard scenes were replaced with demonstrated cards and sessions.

Initial headless Chrome received App Check HTTP 403 and failed account reads. A regular headed Chrome Playwright session succeeded without bypassing verification or changing site security. This is a capture-environment observation, not evidence that all environments work.

The project's existing `docs/media/images` and `docs/media/videos` are promotional illustrations / animated recreations according to its own media README. None was substituted for a live UI screenshot.

## Robot Arm Studio

- Updated source: `20261015_194516_1.mp4`, GitHub attachment ID `d4cfe535-e3a1-4447-85e7-e06dfd3d00e5`; 2160×3840, approximately 22.95 seconds. Downloaded successfully using the owner's existing GitHub authorization. Shows the assembled arm with its complete gripper.
- `robot-assembled.mp4`: complete source sequence, resized to 720×1280, 30 fps, H.264 CRF 18, no audio. This is the profile's linked robot video.
- `robot-arm.jpg`: frame at approximately 15 seconds from that source.
- `robot-motion.gif`: approximately seconds 12–17, 360 pixels wide, 10 fps, 80-color palette. Genuine recorded movement, not animation generated from a still. The earlier partial-arm recording is no longer the profile preview.
- Legacy names `robot-and-controller.jpg`, `robot-control.gif`, `robot-control-demo.mp4` and `robot-motion-demo.mp4` are absent from current source main. They were removed from the profile links.
- Mechanical design credit: [FABRI_CREATOR](https://cults3d.com/en/3d-model/gadget/brazo-robotico-con-arduino-step-files-robotic-arm-guardar-reproducir-export). No purchased CAD/STL is redistributed. See the source repository's [attribution](https://github.com/AdamAbuToamy/RobotArmStudio/blob/main/ATTRIBUTION.md).

## FPV Drone

- `drone-build.jpg`: resized/recompressed derivative of [docs/media/20260903_023031.jpg](https://github.com/AdamAbuToamy/FPV-Drone/blob/main/docs/media/20260903_023031.jpg), an original build/soldering photograph. Original dimensions 4000×3000; orientation handled by the existing source pixels.
- Six original photographs were inventoried; source images were not edited in their repository.
- Legacy names `drone-built.jpg`, `drone-bench-demo.mp4` and `betaflight-orientation-demo.mp4` are absent from current source main.
- Earlier unauthenticated attachment requests returned 404. The updated original recordings were subsequently downloaded successfully with the owner's existing GitHub authorization. No credentials are published.
- Selected source: `20260905_015915.mp4`, attachment ID `4fea01d5-7573-4ffe-8d09-32b068560a1e`; 3840×2160, approximately 12.267 seconds. Visual inspection shows the physical drone being tilted while Betaflight's 3D model responds. This is an orientation/accelerometer check, not a throttle, flight or calibrated acceleration-performance test.
- `drone-betaflight.mp4`: complete sequence, resized to 1920×1080, 30 fps, H.264 CRF 18, no audio. `drone-betaflight.gif` is a real five-second excerpt, approximately seconds 4–9, 640 pixels wide, 8 fps. `drone-betaflight.jpg` is a source frame at approximately 7 seconds.

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
