# Videos HyperFrames

Proyectos de video creados con [HyperFrames](https://hyperframes.heygen.com).

## Videos

- `videos/presupuesto-emergencia-el-nino/` — «Ante una emergencia, prioriza lo esencial».
  Video educativo vertical (1080×1920, 60 s) sobre presupuesto familiar de emergencia
  ante posibles afectaciones del fenómeno de El Niño en Ecuador.
  - Video final: `renders/ante-una-emergencia-prioriza-lo-esencial.mp4`
  - Texto de locución: `renders/locucion.txt`
  - Plan y guion: `BRIEF.md`, `STORYBOARD.md`, `SCRIPT.md`

- `videos/smb-app-movil-promo/` — Promoción de la App Móvil de la Cooperativa San Miguel de los Bancos.
  Video vertical (1080×1920, 27,5 s) estilo Apple con tipografía Poppins.
  - Video final (v2, sin locución): `renders/app-movil-san-miguel-de-los-bancos-v2.mp4`
  - Versión anterior con voz: `renders/app-movil-san-miguel-de-los-bancos-con-voz.mp4` (ElevenLabs, voz Daniela)
  - Versión sin audio: `renders/app-movil-san-miguel-de-los-bancos.mp4`
  - Plan: `BRIEF.md`, `STORYBOARD.md`; bocetos en `boards/storyboard.html`

- `videos/lente-directo-banner/` — Banner animado para la suscripción de Facebook de Lente Directo (overlay de OBS).
  1920×175 px exactos, 30 s, voz Pedro Alejandro + música y efectos (ElevenLabs).
  - `renders/lente-directo-banner-1920x175.mp4` — con audio (H.264 4:4:4)
  - `renders/lente-directo-banner-1920x175-sin-audio.mp4` — sin audio, para bucle en el live
  - `renders/lente-directo-banner-1920x175.webm` — VP9 con audio
  - `renders/lente-directo-banner-1920x176-compatible.mp4` — 1920×176 para reproductores que exigen altura par

## Skills

Las skills de HyperFrames están en `.agents/skills/` (enlazadas desde `.claude/skills/`),
así se cargan solas al abrir este repositorio en una sesión de Claude Code.

## Recetas guardadas

`.media/recipes/explicativo-institucional-vertical/` guarda el estilo de este video
(vertical 1080×1920, español, voz `ef_dora`, azul oscuro, verde y blanco, plantilla de rubros).
Para un video nuevo con el mismo estilo, abre una sesión con este repositorio y pide:
«haz otro video como la última vez» y entrega tu guion.

`.media/recipes/promo-app-vertical-apple/` guarda el estilo del video de la App Móvil SMB
(vertical, estilo Apple, tipografía Poppins). Pide: «haz una promo como la de la App Móvil».
