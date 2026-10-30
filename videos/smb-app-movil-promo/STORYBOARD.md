---
format: 1080x1920
duration: 27.5s
message: "Tu cooperativa en tu bolsillo: la nueva App Móvil de San Miguel de los Bancos, disponible en App Store y Google Play."
arc: Hook → Product intro → Acceso → Mis productos → Funciones → Transferencias al instante → CTA
audience: Socios y potenciales socios de la Cooperativa San Miguel de los Bancos
mode: collaborative
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

- scene: Logo de la cooperativa arriba; la frase aparece en tres golpes: «Tu cooperativa» / «al alcance de» / «tu bolsillo.» con «bolsillo» en verde.
- voiceover: "Tu cooperativa, al alcance de tu bolsillo."
- duration: 3s
- transition_in: cut
- status: animated
- src: compositions/frames/01-apertura.html
- type: hook
- persuasion: Future pacing
- beat: curiosity
- asset_candidates: capture/assets/logo-smb.png — logo de la cooperativa
- on_screen: "Tu cooperativa" / "al alcance de" / "tu bolsillo."

narrativeRole: Abre con la promesa en lenguaje del socio, sin nombrar todavía la app.
keyMessage: Tu cooperativa ahora cabe en tu teléfono.

- blueprint: kinetic-type-beats (Adapt)
- focal: la frase en tres líneas
- roles: titular = foreground subject · logo = supporting (arriba) · fondo claro = background

Scene 1 (0.0–0.6s): el logo aparece arriba con desenfoque que se aclara y leve escala 0.96→1.
Scene 2 (0.5–2.0s): «Tu cooperativa» entra (blur→0 + subida); a 0.9s «al alcance de»; a 1.3s «tu bolsillo.» y la palabra «bolsillo.» se tiñe de verde #2F8A00 con un barrido de izquierda a derecha.
Scene 3 (2.0–3.0s): hold quieto.

## Frame 2 — La nueva app

- scene: El teléfono con la pantalla de ingreso sube desde abajo y gira suavemente hasta quedar de frente, centrado; arriba aparece el título (sin logo).
- voiceover: "Accede a la App Móvil de tu Cooperativa San Miguel de los Bancos."
- duration: 4s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-la-nueva-app.html
- type: product_intro
- persuasion: Show-don't-tell proof
- beat: aspiration
- asset_candidates: capture/assets/phone-login.png — teléfono con la pantalla de ingreso
- on_screen: "Accede a la App Móvil" / "de tu Cooperativa San Miguel de los Bancos"

narrativeRole: Presenta el producto como protagonista, con la marca y su lema.
keyMessage: Esta es la nueva App Móvil de San Miguel de los Bancos.

- blueprint: device-surface-showcase (Adapt)
- focal: el teléfono con la pantalla de ingreso
- roles: teléfono = foreground subject · titular y subtítulo = supporting arriba

Scene 1 (0.0–1.4s): el teléfono sube desde abajo (y +500px), con rotación 3D suave (rotateY 18°→0, rotateX 8°→0, escala 0.9→1) y su sombra crece; llegada expo.out.
Scene 2 (0.6–1.8s): «Accede a la App Móvil» entra con blur→0; a 1.0s «de tu Cooperativa» y a 1.3s «San Miguel de los Bancos» en verde.
Scene 3 (1.8–4.0s): un brillo de luz diagonal cruza una sola vez la pantalla del teléfono (shimmer sutil, 0.8s); luego hold.

## Frame 3 — Acceso fácil

- scene: Acercamiento a los botones de ingreso; se iluminan uno a uno Usuario y contraseña, Huella dactilar y Pagar con QR mientras aparecen «fácil», «rápida» y «segura».
- voiceover: "Ingresa de forma fácil, rápida y segura."
- duration: 4s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/03-acceso.html
- type: feature_showcase
- persuasion: Friction reduction
- beat: ease
- asset_candidates: capture/assets/login-opciones.png — los 4 botones de ingreso
- on_screen: "Accede de forma" / "fácil, rápida y segura."

narrativeRole: Muestra que entrar y pagar es inmediato.
keyMessage: Ingresar y pagar toma un toque.

- blueprint: kinetic-type-beats (Adapt)
- focal: la tarjeta con los 4 botones de ingreso
- roles: tarjeta = foreground subject · marco verde = supporting (indicador) · titulares = supporting arriba

Scene 1 (0.0–0.8s): «Accede de forma» entra; la tarjeta de botones llega con escala 1.08→1 y blur→0 (sensación de acercamiento).
Scene 2 (0.8–3.2s): la línea verde se construye palabra a palabra «fácil,» (0.8s) «rápida» (1.4s) «y segura.» (2.0s); al mismo tiempo el marco verde #4DC600 recorre los botones: Usuario y contraseña (0.8s) → Huella dactilar (1.4s) → Pagar con QR (2.0s), deslizándose suave entre ellos; el botón marcado sube 1.04.
Scene 3 (3.2–4.0s): el marco queda en Huella dactilar como en el boceto; hold.

## Frame 4 — Mis productos

- scene: Cambio a la pantalla de inicio; la tarjeta «Mis productos» (Todos, Cuentas, Créditos) se acerca en primer plano.
- voiceover: "Revisa tu saldo, tus créditos, inversiones y mucho más."
- duration: 4s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-mis-productos.html
- type: feature_showcase
- persuasion: Feature-to-benefit translation
- beat: control
- asset_candidates: capture/assets/phone-home.png — pantalla de inicio; capture/assets/home-productos.png — pestañas y tarjeta de ahorro
- on_screen: "Revisa tu saldo," / "créditos, inversiones y más."

narrativeRole: El socio ve y controla sus productos en un solo lugar.
keyMessage: Todos tus productos, en una pantalla.

- blueprint: device-surface-showcase (Adapt)
- focal: la tarjeta «Mis productos»
- roles: tarjeta = foreground subject · titulares = supporting arriba

Scene 1 (0.0–0.8s): «Revisa tu saldo,» entra con blur→0.
Scene 2 (0.5–2.2s): la tarjeta de productos llega desde abajo con escala 0.9→1 y sombra creciente; a 0.9s entra «créditos, inversiones» y a 1.3s «y más.».
Scene 3 (2.2–4.0s): dentro de la tarjeta, un resalte verde suave (anillo #4DC600 al 60%) se posa sobre el saldo disponible y se queda; hold.

## Frame 5 — Todo lo que necesitas

- scene: Las 9 funciones del menú «¿Qué te gustaría hacer?» se ensamblan en cascada en una cuadrícula 3×3 grande; Transferir y Pagar Servicios se destacan primero.
- voiceover: "Transfiere, paga tus servicios y gestiona todo desde tu app."
- duration: 5s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/05-funciones.html
- type: feature_showcase
- persuasion: Value stacking
- beat: confidence
- asset_candidates: capture/assets/tile-transferir.png — Transferir; capture/assets/tile-pagar-servicios.png — Pagar Servicios; capture/assets/tile-wipea.png — WIPEA; capture/assets/tile-wallet-joven.png — Wallet joven; capture/assets/tile-verificar.png — Verificar Transferencias; capture/assets/tile-rapidito.png — Rapidito; capture/assets/tile-estado-cuenta.png — Estado de cuenta; capture/assets/tile-certificado.png — Certificado Bancario; capture/assets/tile-cuentas-hijos.png — Crear cuentas hijos
- on_screen: "Transfiere. Paga. Gestiona." / "Todo desde tu app."

narrativeRole: Demuestra la amplitud de funciones de un vistazo.
keyMessage: Todo lo que haces en la agencia, ahora en la app.

- blueprint: grid-card-assemble (Reproduce)
- focal: la cuadrícula de 9 funciones
- roles: 9 tarjetas = foreground subject · titulares = supporting arriba

Scene 1 (0.0–0.9s): «Transfiere.» (0.0) «Paga.» (0.3) «Gestiona.» (0.6) entran por golpes.
Scene 2 (0.7–2.6s): las 9 tarjetas aparecen en cascada diagonal (desde arriba-izquierda), cada una con escala 0.85→1, blur→0 y subida 40px, stagger ~0.12s.
Scene 3 (2.6–5.0s): «Todo desde tu app.» entra en 2.6s; hold quieto.

## Frame 6 — Transferencias al instante

- scene: «Transferencias al instante.» en grande; solo la tarjeta Transferir al centro; debajo, una moneda viaja de la billetera al destino bajo un cronómetro que da una vuelta rápida y termina en un check verde.
- voiceover: "Con WIPEA, tus transferencias llegan al instante."
- duration: 4s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-transferencias.html
- type: benefit_highlight
- persuasion: Speed promise (Friction reduction)
- beat: excitement
- asset_candidates: capture/assets/tile-transferir.png — Transferir
- on_screen: "Transferencias" / "al instante."

narrativeRole: Destaca la rapidez de las transferencias con WIPEA.
keyMessage: Transfiere al instante desde la app.

- blueprint: kinetic-type-beats (Adapt)
- focal: «Transferencias al instante.» + las dos tarjetas
- roles: titular = foreground subject · tarjetas WIPEA y Transferir = supporting · flecha verde = movimiento firma

Scene 1 (0.0–0.9s): «Transferencias» entra rápido (expo.out, blur 20→0); a 0.35s «al instante.» en verde.
Scene 2 (0.8–1.8s): las tarjetas WIPEA (izquierda) y Transferir (derecha) llegan desde los lados hacia su posición.
Scene 3 (1.8–4.0s): la flecha verde se dibuja veloz bajo las tarjetas (0.35s) con una estela de movimiento; luego un pequeño destello verde en Transferir; hold.

## Frame 7 — Descárgala

- scene: Los dos teléfonos (ingreso e inicio) lado a lado, levemente inclinados; debajo «Descárgala ya.» y las insignias oficiales de App Store y Google Play (sin logo).
- voiceover: "Descárgala ya en App Store y Google Play."
- duration: 3.5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-descargala.html
- type: cta
- persuasion: Call to act
- beat: motivation
- asset_candidates: capture/assets/phone-login.png — pantalla de ingreso; capture/assets/phone-home.png — pantalla de inicio; capture/assets/badge-app-store.svg — insignia oficial App Store; capture/assets/badge-google-play.svg — insignia oficial Google Play
- on_screen: "Descárgala ya." / "Disponible en App Store y Google Play"

narrativeRole: Cierra con la acción concreta y dónde descargarla.
keyMessage: Disponible en App Store y Google Play.

- blueprint: logo-assemble-lockup (Adapt — sin logo: el cierre son los teléfonos + insignias)
- focal: los dos teléfonos
- roles: teléfonos = foreground subject · «Descárgala ya.» = supporting · insignias = CTA

Scene 1 (0.0–1.2s): los dos teléfonos llegan desde abajo y desde los lados hasta su inclinación ±6°, con escala 0.9→1 (expo.out).
Scene 2 (0.9–1.8s): «Descárgala ya.» entra con blur→0.
Scene 3 (1.5–3.5s): las insignias App Store (1.5s) y Google Play (1.7s) suben y aparecen; hold final quieto, con un fundido suave a fondo claro en los últimos 0.3s.
