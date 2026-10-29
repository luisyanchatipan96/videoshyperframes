# Videos HyperFrames — instrucciones para Claude

Repositorio de videos hechos con HyperFrames. Cada video vive en su carpeta `videos/<nombre-del-video>/`.
Las skills de HyperFrames están en `.agents/skills/` (enlazadas desde `.claude/skills/`).
Responde al usuario en español.

## Al empezar un video nuevo

1. Instala la receta guardada en el nivel de usuario (el contenedor es nuevo en cada sesión):
   `mkdir -p ~/.media/recipes && cp -a .media/recipes/* ~/.media/recipes/`
2. Sigue `/hyperframes`. Si el usuario pide "como la última vez" o un video del mismo estilo,
   ofrece la receta `explicativo-institucional-vertical` (faceless-explainer, 1080×1920, español,
   voz Kokoro `ef_dora` a velocidad 0.92, preset blue-professional con azul #0B2545, verde #23963F y blanco).
   Para promociones de apps o productos, ofrece la receta `promo-app-vertical-apple` (product-launch-video,
   1080×1920, español, estilo Apple: fondo #F5F5F7, tipografía Poppins, sin audio por defecto; base en
   `videos/smb-app-movil-promo/`). Con mockups .ai: son PDF; extrae con `pdftocairo -png -transp`.
3. Crea el proyecto en `videos/<nombre>/` con `npx hyperframes init`.

## Particularidades de este entorno en la nube (aprendidas en el primer video)

- Sin cuenta HeyGen: la voz se genera local con Kokoro. Instala primero `pip install kokoro-onnx soundfile`.
- `huggingface.co` y `cdn.jsdelivr.net` están bloqueados por la red:
  - No hay transcripción automática; para tiempos por palabra usa
    `python3 -I tools/estimar-tiempos-palabras.py <proyecto>` (pausas del audio + texto exacto de SCRIPT.md).
    Vuelve a ejecutarlo después de `audio.mjs fetch-sfx`, que borra las palabras de `audio_meta.json`.
  - GSAP debe ir local: copia `assets/vendor/gsap.min.js` de un video existente y, después de
    `assemble-index.mjs`, reemplaza la URL de jsdelivr por `assets/vendor/gsap.min.js` en `index.html` y las composiciones.
  - Fuentes: copia `assets/fonts/` de un video existente (Space Grotesk e Inter en .woff2).
- El verde #2BA84A no cumple contraste como texto sobre blanco; usa #23963F.
- Al terminar, haz commit y push: el contenedor se borra al cerrar la sesión.
