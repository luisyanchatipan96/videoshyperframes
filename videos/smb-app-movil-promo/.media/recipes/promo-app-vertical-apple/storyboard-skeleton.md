---
format: 1080x1920
duration: 27.5s
arc: Hook → Product intro → Acceso → Mis productos → Funciones → Transferencias al instante → CTA
music: none
---

## Video direction

- look: estilo keynote/anuncio de Apple. Fondo claro (#F5F5F7 con un leve brillo radial blanco arriba), mucho aire, una sola idea por plano, el producto real (teléfonos y tarjetas del mockup) como héroe con sombra suave azulada. Sin texturas, sin rejillas, sin degradados morados.
- palette (frame.md): titulares en azul de marca #04478C; palabra clave en verde texto #2F8A00; verde vivo #4DC600 solo para formas (marcos, flechas, puntos); texto secundario #5B6B7F.
- type: Poppins (assets/fonts/Poppins_400…800.woff2). Titulares 700, tracking −0.03em; subtítulos 600/500. Los textos van EXACTOS como en el boceto confirmado.
- motion grammar: movimientos de Apple — entradas con desenfoque que se aclara (blur 16px→0 + opacidad + subida 50px), escala suave del producto (0.92→1), curvas largas sin rebote (power3.out / expo.out en llegadas rápidas). Palabras de titular por golpes: cada línea entra sola, una tras otra. Nada de rebotes, nada de "respirar". En el hold, quieto.
- rhythm: 01 y 07 calmas; 02–06 cada una con un movimiento firma (giro del teléfono, recorrido del marco verde, acercamiento de la tarjeta, cascada de 9 tarjetas, flecha veloz).
- layout: respetar las posiciones de los bocetos confirmados (boards/stills). Sin subtítulos; todo el contenido entre y≈180 y y≈1700.
- negative list: sin logos de terceros salvo las insignias oficiales; no inventar cifras ni funciones; no deformar imágenes del mockup (escala uniforme); sin rebotes; ni slideshow (todo en t=0 y congelado) ni salvapantallas.

## Frame 1 — Apertura

- duration: 3s
- transition_in: cut
- status: outline
- src: compositions/frames/01-apertura.html
- type: hook
- persuasion: Future pacing
- beat: curiosity
- on_screen: "Tu cooperativa" / "al alcance de" / "tu bolsillo."

<fill in: this video's content for the "Apertura" beat — keep the layout role, replace the words.>

- blueprint: kinetic-type-beats (Adapt)
- focal: la frase en tres líneas
- roles: titular = foreground subject · logo = supporting (arriba) · fondo claro = background

## Frame 2 — La nueva app

- duration: 4s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-la-nueva-app.html
- type: product_intro
- persuasion: Show-don't-tell proof
- beat: aspiration
- on_screen: "Accede a la App Móvil" / "de tu Cooperativa San Miguel de los Bancos"

<fill in: this video's content for the "La nueva app" beat — keep the layout role, replace the words.>

- blueprint: device-surface-showcase (Adapt)
- focal: el teléfono con la pantalla de ingreso
- roles: teléfono = foreground subject · titular y subtítulo = supporting arriba

## Frame 3 — Acceso fácil

- duration: 4s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/03-acceso.html
- type: feature_showcase
- persuasion: Friction reduction
- beat: ease
- on_screen: "Accede de forma" / "fácil, rápida y segura."

<fill in: this video's content for the "Acceso fácil" beat — keep the layout role, replace the words.>

- blueprint: kinetic-type-beats (Adapt)
- focal: la tarjeta con los 4 botones de ingreso
- roles: tarjeta = foreground subject · marco verde = supporting (indicador) · titulares = supporting arriba

## Frame 4 — Mis productos

- duration: 4s
- transition_in: crossfade
- status: outline
- src: compositions/frames/04-mis-productos.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation
- beat: control
- on_screen: "Revisa tu saldo," / "créditos, inversiones y más."

<fill in: this video's content for the "Mis productos" beat — keep the layout role, replace the words.>

- blueprint: device-surface-showcase (Adapt)
- focal: la tarjeta «Mis productos»
- roles: tarjeta = foreground subject · titulares = supporting arriba

## Frame 5 — Todo lo que necesitas

- duration: 5s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/05-funciones.html
- type: feature_showcase
- persuasion: Value stacking
- beat: confidence
- on_screen: "Transfiere. Paga. Gestiona." / "Todo desde tu app."

<fill in: this video's content for the "Todo lo que necesitas" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Reproduce)
- focal: la cuadrícula de 9 funciones
- roles: 9 tarjetas = foreground subject · titulares = supporting arriba

## Frame 6 — Transferencias al instante

- duration: 4s
- transition_in: crossfade
- status: outline
- src: compositions/frames/06-transferencias.html
- type: benefit_highlight
- persuasion: Speed promise (Friction reduction)
- beat: excitement
- on_screen: "Transferencias" / "al instante."

<fill in: this video's content for the "Transferencias al instante" beat — keep the layout role, replace the words.>

- blueprint: kinetic-type-beats (Adapt)
- focal: «Transferencias al instante.» + las dos tarjetas
- roles: titular = foreground subject · tarjetas WIPEA y Transferir = supporting · flecha verde = movimiento firma

## Frame 7 — Descárgala

- duration: 3.5s
- transition_in: crossfade
- status: outline
- src: compositions/frames/07-descargala.html
- type: cta
- persuasion: Call to act
- beat: motivation
- on_screen: "Descárgala ya." / "Disponible en App Store y Google Play"

<fill in: this video's content for the "Descárgala" beat — keep the layout role, replace the words.>

- blueprint: logo-assemble-lockup (Adapt — sin logo: el cierre son los teléfonos + insignias)
- focal: los dos teléfonos
- roles: teléfonos = foreground subject · «Descárgala ya.» = supporting · insignias = CTA
