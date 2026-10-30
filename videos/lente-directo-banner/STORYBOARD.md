---
format: 1920x175
duration: 30s
message: "Suscríbete a Lente Directo en Facebook por US$2,99 al mes: contenido exclusivo, videos en vivo e insignia de suscriptor."
arc: Hook → Comunidad → Beneficios → Precio → Botón → Cierre CTA
audience: Seguidores de la página de Facebook Lente Directo (audiencia del live en OBS)
mode: collaborative
music: none
---

## Video direction

- canvas: banner 1920×175 px (franja horizontal para OBS). Fondo #e2b176 con un brillo radial más claro al centro (#EDC28C) y bordes algo más oscuros (#D7A367), siempre en su propio clip de fondo.
- layout fijo (igual en todas las escenas, como en los bocetos confirmados): logo blanco a la izquierda (x 120, alto 135), divisor fino oscuro en x 285, texto central entre x 330 y 1530, zona derecha x 1440–1800 para el símbolo de Facebook y/o el botón «Suscribirte» (azul #1877F2 con la insignia turquesa #14B798). Márgenes seguros: x ≥ 110 y ≤ 1810, y 14–161.
- type: Poppins (assets/fonts/Poppins_400…800.woff2). Texto principal negro #141414; palabras destacadas en blanco con sombra suave. Sin azul en los textos.
- motion grammar: entradas con profundidad — desenfoque que se aclara (blur 12px→0) + opacidad + desplazamiento corto (x 40px o y 24px) + escala 0.96→1, curvas largas sin rebote (power3.out / expo.out). Brillos sutiles: un barrido de luz blanca diagonal (shimmer) una sola vez sobre el elemento clave. Nada de rebotes exagerados ni "respiración" constante; el único latido permitido es el pulso del botón en las escenas 5 y 6 (2 pulsos suaves 1→1.05→1, no infinito).
- continuidad: el logo y el divisor están en la misma posición en todas las escenas. En la escena 1 el logo entra; en las escenas 2–6 ya está presente desde t=0 (sin re-entrada) para que el corte entre escenas no lo haga parpadear.
- audio: la locución, la música y los efectos los coloca el orquestador en la raíz; ningún elemento de audio dentro de los frames.
- negative list: no textos pequeños ilegibles (mínimo 32 px), no beneficios inventados, no saturar con partículas, no rebotes, ni slideshow (todo en t=0 y congelado) ni salvapantallas.

## Frame 1 — Apertura

- scene: Una línea de luz blanca barre el fondo; el logo entra con elegancia y la frase aparece en dos líneas.
- voiceover: "Las historias que importan merecen llegar más lejos."
- duration: 3.7s
- transition_in: cut
- status: built
- src: compositions/frames/01-apertura.html
- type: hook
- persuasion: Purpose framing
- beat: aspiration
- asset_candidates: capture/assets/logo-lente-directo.png — logo
- on_screen: "Las historias que importan" / "merecen llegar más lejos."

narrativeRole: Apertura.
keyMessage: Las historias que importan merecen llegar más lejos.

- blueprint: titlecard-reveal (Adapt)
- focal: la frase en dos líneas
- roles: frase = foreground subject · logo y divisor = supporting · línea de luz = background accent

Scene 1 (0.0–0.9s): el fondo arranca un poco más oscuro y se ilumina (brillo radial sube); una línea de luz blanca recorre de izquierda a derecha en y≈87 (0.2–1.2s).
Scene 2 (0.3–1.0s): el logo entra con escala 0.9→1 + blur→0; el divisor crece de alto 0→99.
Scene 3 (0.4–2.2s): «Las historias que importan» entra (blur + subida) a 0.4s; «merecen llegar más lejos.» a 1.6s.
Scene 4 (2.2–3.7s): hold quieto.

## Frame 2 — Crecemos junto a ti

- scene: Entra el símbolo de Facebook; el nombre Lente Directo se destaca en la frase.
- voiceover: "En Lente Directo crecemos junto a ti, y queremos llevarte la mejor transmisión."
- duration: 5.3s
- transition_in: crossfade
- status: built
- src: compositions/frames/02-crecemos.html
- type: product_intro
- persuasion: Community appeal
- beat: belonging
- asset_candidates: capture/assets/logo-lente-directo.png — logo; capture/assets/facebook-logo.svg — símbolo de Facebook
- on_screen: "En Lente Directo crecemos junto a ti"

narrativeRole: Crecemos junto a ti.
keyMessage: En Lente Directo crecemos junto a ti, y queremos llevarte la mejor transmisión.

- blueprint: kinetic-type-beats (Adapt)
- focal: la frase «En Lente Directo crecemos junto a ti»
- roles: frase = foreground subject · símbolo de Facebook = supporting (derecha) · logo = supporting (fijo)

Scene 1 (0.0–0.8s): la frase entra palabra a palabra en tres golpes: «En» (0.1s), «Lente Directo» (0.3s, en blanco, con un barrido de brillo a 0.9s), «crecemos junto a ti» (0.55s).
Scene 2 (0.8–1.6s): el símbolo de Facebook entra con rotación 3D breve (rotateY 90°→0) + escala 0.6→1 + blur→0; un anillo de luz se expande una vez desde él y se desvanece.
Scene 3 (1.6–5.3s): hold quieto.

## Frame 3 — Beneficios

- scene: Los tres beneficios reales de la suscripción aparecen uno a uno con su icono: Contenido exclusivo, Videos en vivo, Insignia de suscriptor.
- voiceover: "Al suscribirte, disfrutas de contenido exclusivo, videos en vivo y tu insignia de suscriptor."
- duration: 6.5s
- transition_in: crossfade
- status: built
- src: compositions/frames/03-beneficios.html
- type: feature_showcase
- persuasion: Value stacking
- beat: confidence
- asset_candidates: capture/assets/logo-lente-directo.png — logo; capture/assets/icono-candado.svg — candado; capture/assets/icono-video-vivo.svg — cámara en vivo; capture/assets/insignia-suscriptor.svg — insignia turquesa
- on_screen: "Contenido exclusivo" / "Videos en vivo" / "Insignia de suscriptor"

narrativeRole: Beneficios.
keyMessage: Al suscribirte, disfrutas de contenido exclusivo, videos en vivo y tu insignia de suscriptor.

- blueprint: grid-card-assemble (Reproduce)
- focal: los tres beneficios con icono
- roles: tres ítems = foreground subject · logo = supporting (fijo)

Scene 1 (0.0–0.4s): solo logo y divisor.
Scene 2 (0.4–5.0s): cada beneficio entra cuando la voz lo nombra: «Contenido exclusivo» (2.1s), «Videos en vivo» (3.75s), «Insignia de suscriptor» (4.8s). Cada uno: el círculo del icono aparece con escala 0.6→1, el icono con un leve giro que se endereza, la etiqueta con blur→0 + desplazamiento x 30px. Al aparecer, un destello breve blanco recorre su círculo.
Scene 3 (5.0–6.5s): los tres quedan visibles y quietos; el punto rojo de «en vivo» parpadea suave 2 veces (opacidad 1→0.4→1).

## Frame 4 — Precio

- scene: El precio aparece con énfasis y un destello suave; debajo, «Cancela cuando quieras».
- voiceover: "Todo por solo dos dólares con noventa y nueve al mes, y puedes cancelar cuando quieras."
- duration: 5.6s
- transition_in: crossfade
- status: built
- src: compositions/frames/04-precio.html
- type: feature_showcase
- persuasion: Price anchoring + risk reversal
- beat: ease
- asset_candidates: capture/assets/logo-lente-directo.png — logo; capture/assets/facebook-logo.svg — símbolo de Facebook
- on_screen: "Suscríbete por US$2,99 al mes" / "Cancela cuando quieras"

narrativeRole: Precio.
keyMessage: Todo por solo dos dólares con noventa y nueve al mes, y puedes cancelar cuando quieras.

- blueprint: dataviz-countup (Adapt — sin conteo: el precio es un dato fijo)
- focal: «US$2,99»
- roles: precio = foreground subject · «Suscríbete por» / «al mes» = supporting · «Cancela cuando quieras» = supporting · símbolo de Facebook = supporting

Scene 1 (0.0–0.8s): «Suscríbete por» entra desde la izquierda con blur→0.
Scene 2 (0.9–2.0s): «US$2,99» entra con profundidad (escala 1.3→1, blur 14→0, opacidad) y un destello suave de luz blanca lo cruza a 1.5s; «al mes» entra a 1.3s.
Scene 3 (3.4–4.2s): «Cancela cuando quieras» sube y aparece cuando la voz lo dice.
Scene 4 (0.9s): el símbolo de Facebook aparece con fundido + escala 0.8→1 a la derecha. Hold hasta 5.6s.

## Frame 5 — Comunidad

- scene: El botón «Suscribirte» con la insignia turquesa aparece con una animación llamativa y un pulso sutil.
- voiceover: "Forma parte de nuestra comunidad de suscriptores."
- duration: 3.4s
- transition_in: crossfade
- status: built
- src: compositions/frames/05-comunidad.html
- type: benefit_highlight
- persuasion: Belonging
- beat: motivation
- asset_candidates: capture/assets/logo-lente-directo.png — logo; capture/assets/insignia-suscriptor.svg — insignia turquesa
- on_screen: "Forma parte de nuestra comunidad"

narrativeRole: Comunidad.
keyMessage: Forma parte de nuestra comunidad de suscriptores.

- blueprint: kinetic-type-beats (Adapt)
- focal: el botón «Suscribirte» con la insignia turquesa
- roles: botón = foreground subject (CTA) · frase = supporting · logo = supporting

Scene 1 (0.0–0.8s): «Forma parte de» entra; «nuestra comunidad» en blanco a 0.35s.
Scene 2 (0.5–1.4s): el botón entra llamativo desde la derecha (x +120 → 0, escala 0.8→1, blur→0, expo.out); la insignia turquesa gira 360° una vez al llegar y un barrido de brillo cruza el botón a 1.2s.
Scene 3 (1.6–3.4s): dos pulsos suaves del botón (1→1.05→1) con un halo turquesa que se expande y desaparece; luego quieto.

## Frame 6 — Cierre

- scene: Cierre con logo, símbolo de Facebook y botón «Suscribirte» con insignia turquesa; pausa visual final.
- voiceover: "Haz clic en Suscribirte y sé parte de Lente Directo."
- duration: 5.5s
- transition_in: crossfade
- status: built
- src: compositions/frames/06-cierre.html
- type: cta
- persuasion: Call to act
- beat: urgency-to-act
- asset_candidates: capture/assets/logo-lente-directo.png — logo; capture/assets/facebook-logo.svg — símbolo de Facebook; capture/assets/insignia-suscriptor.svg — insignia turquesa
- on_screen: "Haz clic en Suscribirte"

narrativeRole: Cierre.
keyMessage: Haz clic en Suscribirte y sé parte de Lente Directo.

- blueprint: titlecard-reveal (Adapt)
- focal: «Haz clic en Suscribirte» + botón
- roles: frase = foreground subject · botón = CTA · símbolo de Facebook = supporting · logo = supporting

Scene 1 (0.0–0.9s): «Haz clic en» entra; «Suscribirte» en blanco a 0.35s.
Scene 2 (0.3–1.2s): el símbolo de Facebook y el botón entran juntos (fundido + escala 0.9→1); un cursor-mano blanco NO se usa (mantener limpio).
Scene 3 (1.4–2.6s): un pulso suave del botón con halo turquesa; un barrido de brillo final cruza el botón.
Scene 4 (2.6–5.5s): pausa visual: todo quieto para leer el llamado a la acción. Sin fundido de salida (el banner puede repetirse en bucle en OBS: el último fotograma debe verse completo).
