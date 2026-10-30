---
format: 1080x1920
duration: 60s
message: "En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos: si alguien te pide dinero por WhatsApp a nombre de la cooperativa, es una estafa."
arc: Alerta → Así engañan → La verdad → Señales → Qué hacer → Oficinas → Cierre
audience: Socios y público de la zona (San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito, Mindo)
mode: collaborative
music: none
structure: how-to
---

## Video direction

- look: limpio e institucional (mismo sistema que la App Móvil SMB): fondo #F5F5F7 con brillo radial blanco, Poppins, titulares azul #04478C, verde #4DC600 para lo correcto/seguro, rojo #E5484D SOLO para alertas y estafa. Ilustraciones planas en SVG/CSS, sombras suaves azuladas.
- layout: respetar exactamente los bocetos confirmados (boards/stills). Sin subtítulos; todo el contenido entre y≈150 y y≈1700.
- motion grammar: entradas con desenfoque que se aclara + subida corta, curvas largas sin rebote (power3.out / expo.out). Excepciones con intención: los sellos «¡ALERTA!» y «ESTAFA» caen con un golpe (escala 1.6→1 con un pequeño temblor de 0.15 s). Cada pieza aparece cuando la voz la nombra (tiempos en cada escena). Holds quietos; nada de "respirar".
- reveal timing: los tiempos de cada Scene están ya sincronizados con la locución real (segundos locales de la escena).
- negative list: no logos de terceros reales (el ícono de chat es genérico); no números de teléfono reales (siempre enmascarado); sin datos, montos ni direcciones inventadas; sin rebotes; ni slideshow ni salvapantallas.

## Frame 1 — Alerta

- scene: Un celular vibra y llega una notificación de WhatsApp de «Asesor de Crédito»; aparece un sello «¡ALERTA!».
- voiceover: "¿Te escribieron por WhatsApp diciendo que son asesores de crédito de la Cooperativa San Miguel de los Bancos? ¡Cuidado!"
- duration: 7s
- transition_in: cut
- status: animated
- src: compositions/frames/01-alerta.html
- type: hook
- persuasion: Pattern interrupt
- beat: alarm + curiosity
- on_screen: "¡Alerta!" / notificación "Asesor de Crédito"

narrativeRole: Alerta.
keyMessage: ¿Te escribieron por WhatsApp diciendo que son asesores de crédito de la Cooperativa San Miguel de los Bancos? ¡Cuidado!

- blueprint: kinetic-type-beats (Adapt)
- focal: el celular con la notificación del falso asesor
- roles: celular = foreground subject · sello ¡ALERTA! = accent · pregunta = supporting

Scene 1 (0.0–1.2s): el celular sube desde abajo (y +300, blur→0); en 0.5s vibra (x ±8px, 4 ciclos rápidos, determinista) y la notificación cae desde arriba dentro de la pantalla.
Scene 2 (0.6–3.0s): la pregunta entra línea por línea: «¿Te escribió un» (0.6s), «"asesor de crédito"» (1.3s), «por WhatsApp?» (2.0s).
Scene 3 (6.0s, en «¡Cuidado!»): el sello «¡ALERTA!» cae con golpe sobre la parte superior; hold.

## Frame 2 — Así engañan

- scene: Chat animado: «Hola, soy asesor de la Cooperativa…» → «Para revisar tu buró de crédito debes hacer un depósito»; al final el chat se marca con «ESTAFA».
- voiceover: "Personas que se hacen pasar por la cooperativa te piden dinero para revisar tu buró de crédito o agilizar un trámite. Es una estafa."
- duration: 10s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-asi-enganan.html
- type: pain_point
- persuasion: Show-don't-tell (worked example)
- beat: suspicion
- on_screen: "Así engañan" / chat / "ESTAFA"

narrativeRole: Así engañan.
keyMessage: Personas que se hacen pasar por la cooperativa te piden dinero para revisar tu buró de crédito o agilizar un trámite. Es una estafa.

- blueprint: compose
- focal: el chat de ejemplo
- roles: chat = foreground subject · sello ESTAFA = accent · título = supporting

Scene 1 (0.0–0.8s): «Así engañan» entra; el celular con el chat sube.
Scene 2 (1.0–5.5s): los mensajes llegan uno por uno, cada uno precedido por un indicador «escribiendo…» (tres puntos) de 0.5s: mensaje 1 en 1.0s, mensaje 2 en 2.6s (la palabra «buró de crédito» se resalta en amarillo suave), respuesta verde en 4.0s, mensaje 4 en 5.0s.
Scene 3 (6.1s, en «Es una estafa»): el sello rojo «ESTAFA» cae con golpe sobre el chat; el chat se atenúa al 70 %; hold.

## Frame 3 — La verdad

- scene: Logo de la cooperativa y un sello verde «Todos nuestros trámites son GRATUITOS».
- voiceover: "En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos. Nunca te pediremos dinero por WhatsApp para revisar tu buró ni aprobar un crédito."
- duration: 9s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/03-la-verdad.html
- type: product_intro
- persuasion: Reframe
- beat: relief + trust
- on_screen: "Todos nuestros trámites son" / "GRATUITOS"

narrativeRole: La verdad.
keyMessage: En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos. Nunca te pediremos dinero por WhatsApp para revisar tu buró ni aprobar un crédito.

- blueprint: titlecard-reveal (Adapt)
- focal: el sello verde GRATUITOS
- roles: GRATUITOS = foreground subject · logo y textos = supporting

Scene 1 (0.0–1.0s): el logo entra con blur→0 y escala 0.95→1.
Scene 2 (1.45s): «Todos nuestros trámites son» entra; en 2.75s el bloque verde «GRATUITOS» entra con escala 1.2→1 y un destello blanco que lo cruza.
Scene 3 (3.75s): «Nunca te pediremos dinero por WhatsApp» sube; hold.

## Frame 4 — Señales de alerta

- scene: Cuatro tarjetas con icono entran una a una: te piden depósitos · número desconocido · te presionan con urgencia · te piden claves o códigos.
- voiceover: "Desconfía si te piden depósitos, si te escriben desde números desconocidos, si te presionan para actuar rápido o si te piden claves y códigos."
- duration: 9s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-senales.html
- type: feature_showcase
- persuasion: Checklist (progressive disclosure)
- beat: vigilance
- on_screen: "Señales de alerta" / "Te piden depósitos" / "Número desconocido" / "Te presionan con urgencia" / "Te piden claves o códigos"

narrativeRole: Señales de alerta.
keyMessage: Desconfía si te piden depósitos, si te escriben desde números desconocidos, si te presionan para actuar rápido o si te piden claves y códigos.

- blueprint: grid-card-assemble (Reproduce)
- focal: las 4 tarjetas de señales de alerta
- roles: tarjetas = foreground subject · título = supporting

Scene 1 (0.0–0.8s): «Señales de alerta» entra.
Scene 2 (1.05s, 2.05s, 3.95s, 5.45s): cada tarjeta entra desde la izquierda (x −60, blur→0) cuando la voz la nombra; su icono rojo late una vez (1→1.12→1).
Scene 3: hold.

## Frame 5 — Qué hacer

- scene: Tres acciones con check verde: No transfieras o deposites dinero · No compartas tus datos · Bloquea y contáctanos por nuestros canales oficiales.
- voiceover: "Si te pasa: no transfieras o deposites dinero, no compartas tus datos personales, bloquea el número y contáctanos por nuestros canales oficiales."
- duration: 10s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-que-hacer.html
- type: benefit_highlight
- persuasion: Action steps
- beat: control
- on_screen: "¿Qué hacer?" / "No transfieras o deposites dinero" / "No compartas tus datos" / "Bloquea el número" / "Contáctanos por nuestros canales oficiales"

narrativeRole: Qué hacer.
keyMessage: Si te pasa: no transfieras o deposites dinero, no compartas tus datos personales, bloquea el número y contáctanos por nuestros canales oficiales.

- blueprint: grid-card-assemble (Reproduce)
- focal: las 4 tarjetas de acciones
- roles: tarjetas = foreground subject · título = supporting

Scene 1 (0.0–0.8s): «¿Qué hacer?» entra.
Scene 2 (0.95s, 2.9s, 4.75s, 5.95s): cada tarjeta entra desde la derecha (x +60, blur→0) cuando la voz la nombra; al llegar, un check verde pequeño se dibuja en la esquina derecha de la tarjeta.
Scene 3: hold.

## Frame 6 — Nuestras oficinas

- scene: Mapa ilustrado simple con 4 pines que aparecen uno a uno: San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo.
- voiceover: "Para cualquier trámite, acércate a nuestras oficinas en San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo."
- duration: 9.5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-oficinas.html
- type: cta
- persuasion: Proximity + trust
- beat: confidence
- on_screen: "Visítanos en nuestras oficinas" / "San Miguel de los Bancos" / "Pedro Vicente Maldonado" / "Puerto Quito" / "Mindo" / "Realiza tus trámites de forma presencial y gratuita" (grande)

narrativeRole: Nuestras oficinas.
keyMessage: Para cualquier trámite, acércate a nuestras oficinas en San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo.

- blueprint: compose
- focal: el mapa con 4 pines
- roles: ruta = background accent · pines + nombres = foreground · titular y frase final = supporting

Scene 1 (0.0–0.9s): titular entra; la ruta se dibuja de izquierda a derecha (0.3–1.3s).
Scene 2 (San Miguel de los Bancos 2.55s, Pedro Vicente Maldonado 3.9s, Puerto Quito 5.05s, Mindo 5.65s): cada pin cae desde arriba (y −80 → 0, expo.out) con una onda verde en el suelo y su nombre aparece debajo, cuando la voz lo nombra.
Scene 3 (6.6s): «Realiza tus trámites de forma presencial y gratuita» sube; hold.

## Frame 7 — Cierre

- scene: Ilustración de un asesor sonriente con la credencial de la cooperativa (etiqueta «Asesor de Crédito · Coop. San Miguel de los Bancos»), sin logo; texto grande «Tus trámites son gratuitos».
- voiceover: "Recuerda: tus trámites son gratuitos."
- duration: 5.5s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-cierre.html
- type: branding
- persuasion: Brand recall
- beat: belonging
- on_screen: "Tus trámites son gratuitos"

narrativeRole: Cierre.
keyMessage: Recuerda: tus trámites son gratuitos.

- blueprint: compose
- focal: el asesor ilustrado con la credencial
- roles: asesor = foreground subject · credencial y etiqueta = supporting · titular = supporting

Scene 1 (0.0–1.0s): el asesor sube desde abajo (y +80, blur→0); la credencial se balancea una vez y se asienta (rotación 6°→0 sobre el cordón).
Scene 2 (0.6–1.4s): la etiqueta «Asesor de Crédito · Coop. San Miguel de los Bancos» aparece con escala 0.9→1; el check verde de la credencial hace un brillo.
Scene 3 (0.3s): «Tus trámites son gratuitos» entra; «gratuitos» con un barrido de brillo a 1.2s. Hold final quieto (último fotograma completo, sin fundido).
