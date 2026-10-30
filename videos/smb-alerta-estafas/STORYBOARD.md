---
format: 1080x1920
duration: 60s
message: "En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos: si alguien te pide dinero por WhatsApp a nombre de la cooperativa, es una estafa."
arc: Alerta → Así engañan → La verdad → Señales → Qué hacer → Oficinas → Cierre
audience: Socios y público de la zona (San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito, Mindo)
mode: collaborative
music: calm trustworthy corporate underscore, light piano and soft pads, gentle pulse
structure: how-to
---

## Frame 1 — Alerta

- scene: Un celular vibra y llega una notificación de WhatsApp de «Asesor de Crédito»; aparece un sello «¡ALERTA!».
- voiceover: "¿Te escribieron por WhatsApp diciendo que son asesores de crédito de la Cooperativa San Miguel de los Bancos? ¡Cuidado!"
- duration: 5s
- transition_in: cut
- status: built
- src: compositions/frames/01-alerta.html
- type: hook
- persuasion: Pattern interrupt
- beat: alarm + curiosity
- blueprint: kinetic-type-beats
- on_screen: "¡Alerta!" / notificación "Asesor de Crédito"

narrativeRole: Alerta.
keyMessage: ¿Te escribieron por WhatsApp diciendo que son asesores de crédito de la Cooperativa San Miguel de los Bancos? ¡Cuidado!

## Frame 2 — Así engañan

- scene: Chat animado: «Hola, soy asesor de la Cooperativa…» → «Para revisar tu buró de crédito debes hacer un depósito»; al final el chat se marca con «ESTAFA».
- voiceover: "Personas que se hacen pasar por la cooperativa te piden dinero para revisar tu buró de crédito o agilizar un trámite. Es una estafa."
- duration: 11s
- transition_in: crossfade
- status: built
- src: compositions/frames/02-asi-enganan.html
- type: pain_point
- persuasion: Show-don't-tell (worked example)
- beat: suspicion
- blueprint: compose
- on_screen: "Así engañan" / chat / "ESTAFA"

narrativeRole: Así engañan.
keyMessage: Personas que se hacen pasar por la cooperativa te piden dinero para revisar tu buró de crédito o agilizar un trámite. Es una estafa.

## Frame 3 — La verdad

- scene: Logo de la cooperativa y un sello verde «Todos nuestros trámites son GRATUITOS».
- voiceover: "En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos. Nunca te pediremos dinero por WhatsApp para revisar tu buró ni aprobar un crédito."
- duration: 8s
- transition_in: zoom-through
- status: built
- src: compositions/frames/03-la-verdad.html
- type: product_intro
- persuasion: Reframe
- beat: relief + trust
- blueprint: titlecard-reveal
- on_screen: "Todos nuestros trámites son" / "GRATUITOS"

narrativeRole: La verdad.
keyMessage: En la Cooperativa San Miguel de los Bancos todos los trámites son gratuitos. Nunca te pediremos dinero por WhatsApp para revisar tu buró ni aprobar un crédito.

## Frame 4 — Señales de alerta

- scene: Cuatro tarjetas con icono entran una a una: te piden depósitos · número desconocido · te presionan con urgencia · te piden claves o códigos.
- voiceover: "Desconfía si te piden depósitos, si te escriben desde números desconocidos, si te presionan para actuar rápido o si te piden claves y códigos."
- duration: 14s
- transition_in: crossfade
- status: built
- src: compositions/frames/04-senales.html
- type: feature_showcase
- persuasion: Checklist (progressive disclosure)
- beat: vigilance
- blueprint: grid-card-assemble
- on_screen: "Señales de alerta" / "Te piden depósitos" / "Número desconocido" / "Te presionan con urgencia" / "Te piden claves o códigos"

narrativeRole: Señales de alerta.
keyMessage: Desconfía si te piden depósitos, si te escriben desde números desconocidos, si te presionan para actuar rápido o si te piden claves y códigos.

## Frame 5 — Qué hacer

- scene: Tres acciones con check verde: No transfieras o deposites dinero · No compartas tus datos · Bloquea y contáctanos por nuestros canales oficiales.
- voiceover: "Si te pasa: no transfieras o deposites dinero, no compartas tus datos personales, bloquea el número y contáctanos por nuestros canales oficiales."
- duration: 11s
- transition_in: crossfade
- status: built
- src: compositions/frames/05-que-hacer.html
- type: benefit_highlight
- persuasion: Action steps
- beat: control
- blueprint: grid-card-assemble
- on_screen: "¿Qué hacer?" / "No transfieras o deposites dinero" / "No compartas tus datos" / "Bloquea el número" / "Contáctanos por nuestros canales oficiales"

narrativeRole: Qué hacer.
keyMessage: Si te pasa: no transfieras o deposites dinero, no compartas tus datos personales, bloquea el número y contáctanos por nuestros canales oficiales.

## Frame 6 — Nuestras oficinas

- scene: Mapa ilustrado simple con 4 pines que aparecen uno a uno: San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo.
- voiceover: "Para cualquier trámite, acércate a nuestras oficinas en San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo."
- duration: 9s
- transition_in: crossfade
- status: built
- src: compositions/frames/06-oficinas.html
- type: cta
- persuasion: Proximity + trust
- beat: confidence
- blueprint: compose
- on_screen: "Visítanos en nuestras oficinas" / "San Miguel de los Bancos" / "Pedro Vicente Maldonado" / "Puerto Quito" / "Mindo" / "Realiza tus trámites de forma presencial y gratuita" (grande)

narrativeRole: Nuestras oficinas.
keyMessage: Para cualquier trámite, acércate a nuestras oficinas en San Miguel de los Bancos, Pedro Vicente Maldonado, Puerto Quito y Mindo.

## Frame 7 — Cierre

- scene: Ilustración de un asesor sonriente con la credencial de la cooperativa (etiqueta «Asesor de Crédito · Coop. San Miguel de los Bancos»), sin logo; texto grande «Tus trámites son gratuitos».
- voiceover: "Recuerda: tus trámites son gratuitos."
- duration: 4s
- transition_in: crossfade
- status: built
- src: compositions/frames/07-cierre.html
- type: branding
- persuasion: Brand recall
- beat: belonging
- blueprint: logo-assemble-lockup
- on_screen: "Tus trámites son gratuitos"

narrativeRole: Cierre.
keyMessage: Recuerda: tus trámites son gratuitos.
