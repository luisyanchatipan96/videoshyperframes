---
format: 1080x1920
duration: 60s
arc: Hook → Método (3 pasos) → Alimentación → Salud → Vivienda → Transporte → Ajuste y reserva → Cierre
music: none
title: "Ante una emergencia, prioriza lo esencial"
structure: how-to
---

## Video direction

- palette system (frame.md): canvas blanco `bg` #FFFFFF con un campo azul muy tenue; azul oscuro `text` #0B2545 para títulos, ilustraciones (trazo) y el fondo del cierre; verde `primary` #2BA84A como único acento (lo esencial, checks, monedas, ruta segura); `text-muted` #4A5D78 para subtítulos; tarjetas `card-tinted` (relleno verde 4 %, borde 20 %, radio 14px, sin sombras). Tipografía: display Space Grotesk 700 para títulos y rubros; Inter para subtítulos. Ilustraciones en SVG plano de línea (trazo azul oscuro ~6px, rellenos planos verde/azul tenue, esquinas redondeadas), amables, sin rostros detallados (figuras simples: cabeza circular + cuerpo redondeado).
- ambient layer (todas las escenas salvo el cierre): retícula de puntos azul oscuro al 6 % + un halo radial verde al 8 % en la mitad superior; pequeña barra de progreso verde de 8px en el borde superior (y≈96px) que avanza a lo largo del video.
- plantilla común de RUBRO (escenas 3, 4, 5 y 6 — idéntica, solo cambian ilustración, título y subtítulo; es lo que garantiza IGUAL peso visual): (1) etiqueta-píldora pequeña "Presupuesto de emergencia" centrada en y≈200; (2) TÍTULO del rubro en mayúsculas, display 700, ~120px, azul oscuro, centrado en y≈330; (3) tarjeta-ilustración `card-tinted` centrada, 880×760px, de y≈430 a y≈1190, con la ilustración del rubro dentro; (4) subtítulo Inter 500 ~52px, `text-muted`, centrado, máx. 2 líneas, en y≈1250–1380; (5) fila de 4 chips de rubro iguales (ícono circular 120px + etiqueta 30px: Alimentación, Salud, Vivienda, Transporte, siempre en ese mismo orden de lectura, mismo tamaño), en y≈1420–1560; el chip del rubro actual tiene relleno verde y los otros tres contorno verde — NUNCA cambian de tamaño, ni se numeran, ni se ordenan por prioridad. Nada de "1/4", porcentajes ni montos.
- motion grammar + reveal model: entradas suaves con cola larga (power3.out, fade + subida 40px), sin rebotes ni overshoot. Cada pieza aparece cuando la voz la nombra (los tiempos por escena están abajo); nunca se vuelca todo en t=0. En holds, nada respira: como mucho un jitter mínimo o detalles vivos de SVG (gotas de lluvia lentas, ruedas). Sin paneos ni push en la segunda mitad.
- rhythm / held frames: escena 1 y 8 son calmas (titlecard); escena 2 y 7 construyen; escenas 3–6 tienen el mismo ritmo (mismo template, mismo pulso). El cierre (8) es el beat sostenido.
- negative list: nada alarmista (sin relámpagos, inundaciones, sirenas, rojos, íconos de alerta, signos de exclamación, mapas de riesgo, pronósticos ni fechas de alerta); sin porcentajes, cifras, montos ni gráficos de distribución; sin logotipos (el cierre deja un espacio vacío); sin degradados morados/"IA", sin bokeh; sin rebotes; ni slideshow (todo al inicio y congelado) ni salvapantallas (todo flotando).
- safe zones 1080×1920: márgenes laterales ≥ 90px; contenido clave entre y≈180 y y≈1580; la banda inferior (y > 1594) es de subtítulos — ningún texto ni ilustración importante allí.

## Frame 1 — Apertura

- duration: 6.80s
- transition_in: cut
- status: outline
- src: compositions/frames/01-apertura.html
- type: hook
- persuasion: Reframe (finanzas = cuidado familiar)
- beat: calma y cercanía
- on_screen: "Fenómeno de El Niño" / "Prepara tu presupuesto de emergencia"

<fill in: this video's content for the "Apertura" beat — keep the layout role, replace the words.>

- blueprint: titlecard-reveal (Adapt)
- focal: la familia ilustrada alrededor de la mesa con la libreta
- roles: familia + mesa + libreta = foreground subject · nube de lluvia, casa y calendario = supporting (íconos de línea en arco sobre la familia) · retícula + halo = background

## Frame 2 — Tres pasos

- duration: 7.87s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-tres-pasos.html
- type: product_intro
- persuasion: Progressive disclosure (tres pasos revelados al nombrarse)
- beat: claridad
- on_screen: "Revisa cuánto tienes" / "Identifica lo indispensable" / "Pospón gastos no esenciales"

<fill in: this video's content for the "Tres pasos" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Adapt)
- focal: la libreta con tres apartados
- roles: libreta grande = foreground subject · tres filas (dinero disponible / gastos esenciales / pueden esperar) = supporting · retícula = background

## Frame 3 — Alimentación

- duration: 8.68s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/03-alimentacion.html
- type: feature_showcase
- persuasion: Concretization (lista concreta)
- beat: orden y control
- on_screen: "ALIMENTACIÓN" / "Revisa • Planifica • Compra lo necesario"

<fill in: this video's content for the "Alimentación" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de alimentación (alacena + lista)
- roles: alacena con frascos, lista con checks, bidón de agua segura y latas/granos = foreground subject dentro de la tarjeta · fila de 4 chips (Alimentación activo) = supporting · retícula = background

## Frame 4 — Salud

- duration: 9.17s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/04-salud.html
- type: feature_showcase
- persuasion: Concretization
- beat: cuidado
- on_screen: "SALUD" / "Medicamentos habituales y atención necesaria"

<fill in: this video's content for the "Salud" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de salud (botiquín, receta, calendario de tratamiento)
- roles: botiquín, receta, calendario con días marcados y una moneda que entra al botiquín = foreground subject en la tarjeta · fila de 4 chips (Salud activo) = supporting · retícula = background

## Frame 5 — Vivienda

- duration: 7.33s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/05-vivienda.html
- type: feature_showcase
- persuasion: Concretization
- beat: seguridad
- on_screen: "VIVIENDA" / "Un lugar seguro para tu familia"

<fill in: this video's content for the "Vivienda" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de vivienda (casa con tres símbolos)
- roles: casa central = foreground subject · llave (alquiler), foco + grifo (servicios básicos), cama/carpa (alojamiento temporal) = supporting en arco alrededor de la casa · fila de 4 chips (Vivienda activo) · retícula = background

## Frame 6 — Transporte

- duration: 9.32s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/06-transporte.html
- type: feature_showcase
- persuasion: Concretization
- beat: preparación
- on_screen: "TRANSPORTE" / "Traslados esenciales y salida segura"

<fill in: this video's content for the "Transporte" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: tarjeta-ilustración de transporte (ruta segura)
- roles: ruta punteada verde, autobús y auto = foreground subject · centro de salud (cruz verde) y punto de encuentro (ícono de personas reunidas en un círculo) como destinos = supporting · fila de 4 chips (Transporte activo) · retícula = background

## Frame 7 — Ajusta y reserva

- duration: 6.14s
- transition_in: crossfade
- status: outline
- src: compositions/frames/07-ajusta-reserva.html
- type: benefit_highlight
- persuasion: Synthesis (los cuatro rubros juntos, igual tamaño)
- beat: confianza
- on_screen: "Ajusta según tus necesidades" / "Separa una reserva, si puedes"

<fill in: this video's content for the "Ajusta y reserva" beat — keep the layout role, replace the words.>

- blueprint: constellation-hub (Adapt)
- focal: la libreta del presupuesto familiar al centro
- roles: libreta central = foreground subject · cuatro tarjetas de rubro IDÉNTICAS (mismo tamaño, misma distancia al centro, en cuadrícula 2×2 simétrica) = supporting · frasco de reserva = secondary focal · retícula = background

## Frame 8 — Cierre

- duration: 4.67s
- transition_in: crossfade
- status: outline
- src: compositions/frames/08-cierre.html
- type: cta
- persuasion: Call to act (tríada breve)
- beat: calidez y esperanza
- on_screen: "Planifica hoy." / "Protege lo esencial."

<fill in: this video's content for the "Cierre" beat — keep the layout role, replace the words.>

- blueprint: titlecard-reveal (Reproduce)
- focal: las dos frases de cierre
- roles: fondo azul oscuro #0B2545 = background (full-bleed) · familia pequeña cerrando la libreta = supporting · rectángulo de espacio para logo (vacío, sin borde visible o con borde punteado blanco al 15 %) = reserved
