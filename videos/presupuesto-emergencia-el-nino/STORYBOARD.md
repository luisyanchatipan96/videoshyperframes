---
format: 1080x1920
duration: 60s
message: "Ante una emergencia, prioriza lo esencial: arma un presupuesto familiar de emergencia para alimentación, salud, vivienda y transporte."
arc: Hook → Método (3 pasos) → Alimentación → Salud → Vivienda → Transporte → Ajuste y reserva → Cierre
audience: Familias ecuatorianas
mode: collaborative
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

- scene: Una familia ilustrada (dos adultos, un niño) revisa una libreta de gastos en la mesa; arriba aparecen suavemente una nube de lluvia, una casa y un calendario como íconos lineales.
- voiceover: "Ante posibles afectaciones del fenómeno de El Niño, preparar tus finanzas también es cuidar a tu familia."
- duration: 6.80s
- transition_in: cut
- status: animated
- src: compositions/frames/01-apertura.html
- type: hook
- persuasion: Reframe (finanzas = cuidado familiar)
- beat: calma y cercanía
- on_screen: "Fenómeno de El Niño" / "Prepara tu presupuesto de emergencia"

narrativeRole: Enmarca el tema sin alarma: prepararse financieramente es un acto de cuidado.
keyMessage: Preparar el presupuesto familiar es una forma de proteger a la familia.

- blueprint: titlecard-reveal (Adapt)
- focal: la familia ilustrada alrededor de la mesa con la libreta
- roles: familia + mesa + libreta = foreground subject · nube de lluvia, casa y calendario = supporting (íconos de línea en arco sobre la familia) · retícula + halo = background

Adapt: se conserva el único movimiento sereno del titlecard (slide-up crossfade) para el título; la ilustración se construye antes con svg self-draw.
Scene 1 (0.0–2.4s): centrado, ilustración ~45 % del alto (y≈620–1180): mesa redondeada se dibuja (svg self-draw → svg-path-draw) y la familia (dos adultos y un niño, figuras simples) aparece con fade + subida suave; sobre la mesa una libreta abierta. Al decir "fenómeno de El Niño" (≈1.5s), aparecen en arco sobre ellos tres íconos de línea: nube con gotas lentas, casa, calendario (stagger suave). La píldora "Fenómeno de El Niño" entra en y≈260.
Scene 2 (2.4–5.6s): en "preparar tus finanzas" (≈3.1s) el título "Prepara tu presupuesto de emergencia" (display 700, ~96px, 2–3 líneas, azul oscuro, "emergencia" en verde) entra con slide-up crossfade en y≈330–560. Un adulto señala la libreta; en la libreta aparece un pequeño check verde (svg self-draw).
Scene 3 (5.6–6.8s): en "familia" un corazón pequeño verde aparece sobre la familia; hold quieto, solo gotas de lluvia lentas en la nube (live SVG internals).

## Frame 2 — Tres pasos

- scene: Una libreta abierta con tres apartados que se marcan uno a uno: dinero disponible, gastos esenciales (resaltado en verde) y gastos que pueden esperar (atenuado, se desplaza a un lado).
- voiceover: "Anota cuánto dinero tienes disponible, identifica tus gastos indispensables y pospón las compras que pueden esperar."
- duration: 7.87s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-tres-pasos.html
- type: product_intro
- persuasion: Progressive disclosure (tres pasos revelados al nombrarse)
- beat: claridad
- on_screen: "Revisa cuánto tienes" / "Identifica lo indispensable" / "Pospón gastos no esenciales"

narrativeRole: Entrega el método base antes de entrar en los rubros.
keyMessage: Primero saber cuánto hay, luego separar lo indispensable de lo que puede esperar.

- blueprint: grid-card-assemble (Adapt)
- focal: la libreta con tres apartados
- roles: libreta grande = foreground subject · tres filas (dinero disponible / gastos esenciales / pueden esperar) = supporting · retícula = background

Adapt: la cascada de tarjetas se vuelve tres filas de una libreta que se escriben una a una; firma: ensamblaje escalonado, cada fila al nombrarse.
Scene 1 (0.0–0.5s): libreta (tarjeta blanca con espiral y renglones azules, ~880×1000px, y≈330–1330) sube con fade; encabezado "Mi presupuesto" pequeño arriba de la libreta.
Scene 2 (0.5–2.7s): en "cuánto dinero tienes disponible": fila 1 se escribe (icono billete/monedas verde + "Revisa cuánto tienes", display 600 ~60px) con un check que se dibuja.
Scene 3 (2.7–5.1s): en "identifica tus gastos indispensables" (≈2.7s): fila 2 entra con ícono de canasta+cruz+casa+bus pequeños y "Identifica lo indispensable"; un resaltador verde (css-marker-patterns, highlight sweep) la marca y la fila queda con fondo verde tenue.
Scene 4 (5.1–7.9s): en "pospón" (≈5.1s): fila 3 "Pospón gastos no esenciales" entra con ícono de reloj de arena; luego se atenúa al 45 % y se desplaza 40px a la derecha (pueden esperar). Hold: la fila 2 queda como la más visible.

## Frame 3 — Alimentación

- scene: Plantilla común de rubro: tarjeta grande con ícono de despensa; se revisa una alacena, se marca una lista y aparecen agua segura y alimentos no perecibles. Abajo, un indicador 2×2 de los cuatro rubros, todos del mismo tamaño, con este activo.
- voiceover: "En alimentación, revisa tus reservas y planifica la compra de agua segura y alimentos no perecibles. Evita compras excesivas."
- duration: 8.68s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-alimentacion.html
- type: feature_showcase
- persuasion: Concretization (lista concreta)
- beat: orden y control
- on_screen: "ALIMENTACIÓN" / "Revisa • Planifica • Compra lo necesario"

narrativeRole: Primer rubro esencial; misma plantilla y peso visual que los otros tres.
keyMessage: Comprar lo necesario según lo que ya tienes, sin excesos.

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de alimentación (alacena + lista)
- roles: alacena con frascos, lista con checks, bidón de agua segura y latas/granos = foreground subject dentro de la tarjeta · fila de 4 chips (Alimentación activo) = supporting · retícula = background

Adapt: plantilla común de RUBRO; la ilustración se ensambla por partes al nombrarse.
Scene 1 (0.0–1.1s): píldora, título "ALIMENTACIÓN" y tarjeta vacía entran juntos (fade + subida); la fila de 4 chips ya está presente, el chip Alimentación se rellena de verde.
Scene 2 (1.1–2.4s): en "revisa tus reservas": dentro de la tarjeta, una alacena con dos repisas y frascos aparece (stagger); una lupa pequeña pasa por las repisas.
Scene 3 (2.4–6.4s): en "planifica" (≈2.4s) una lista con 3 renglones aparece a la derecha de la alacena; en "agua segura" (≈3.7s) entra un bidón de agua azul con gota; en "alimentos no perecibles" (≈4.6s) entran latas y un saco de granos; cada uno marca un check verde en la lista. El subtítulo "Revisa • Planifica • Compra lo necesario" aparece palabra por palabra: "Revisa" en 1.1s, "Planifica" en 2.4s, "Compra lo necesario" en 3.7s.
Scene 4 (6.4–8.7s): en "evita compras excesivas": un carrito pequeño con exceso de productos aparece en gris al 40 % y se atenúa (sin tachaduras rojas); hold quieto.

## Frame 4 — Salud

- scene: Misma plantilla de rubro: botiquín, receta y calendario de tratamiento; una porción del presupuesto (sin cifras) se asigna a salud. Indicador 2×2 con salud activo.
- voiceover: "En salud, reserva dinero para medicamentos habituales, insumos básicos y atención necesaria. Considera las necesidades de cada integrante."
- duration: 9.17s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/04-salud.html
- type: feature_showcase
- persuasion: Concretization
- beat: cuidado
- on_screen: "SALUD" / "Medicamentos habituales y atención necesaria"

narrativeRole: Segundo rubro esencial, mismo peso visual.
keyMessage: Reservar para medicamentos y atención según cada integrante.

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de salud (botiquín, receta, calendario de tratamiento)
- roles: botiquín, receta, calendario con días marcados y una moneda que entra al botiquín = foreground subject en la tarjeta · fila de 4 chips (Salud activo) = supporting · retícula = background

Adapt: misma plantilla común de RUBRO.
Scene 1 (0.0–0.7s): píldora, título "SALUD", tarjeta vacía; chip Salud se rellena de verde (los demás contorno).
Scene 2 (0.7–3.2s): en "reserva dinero" una alcancía/sobre pequeño aparece y una moneda verde se desliza hacia un botiquín blanco con cruz verde (no roja) que aparece en "medicamentos habituales" (≈1.9s).
Scene 3 (3.2–6.0s): en "insumos básicos" una receta (hoja con líneas) aparece; en "atención necesaria" (≈4.3s) un calendario de tratamiento con tres días marcados con check verde. El subtítulo "Medicamentos habituales y atención necesaria" entra en 1.9s.
Scene 4 (6.0–9.2s): en "cada integrante": debajo de los objetos, cuatro figuritas simples (adultos, niño, persona mayor) se iluminan una a una; hold quieto.

## Frame 5 — Vivienda

- scene: Misma plantilla de rubro: una casa con tres símbolos (llave de alquiler, foco/grifo de servicios básicos, cama de alojamiento temporal). Indicador 2×2 con vivienda activo.
- voiceover: "En vivienda, contempla alquiler, servicios básicos y un posible alojamiento temporal si debes salir de casa."
- duration: 7.33s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-vivienda.html
- type: feature_showcase
- persuasion: Concretization
- beat: seguridad
- on_screen: "VIVIENDA" / "Un lugar seguro para tu familia"

narrativeRole: Tercer rubro esencial, mismo peso visual.
keyMessage: Contemplar alquiler, servicios y un posible alojamiento temporal.

- blueprint: grid-card-assemble (Adapt)
- focal: tarjeta-ilustración de vivienda (casa con tres símbolos)
- roles: casa central = foreground subject · llave (alquiler), foco + grifo (servicios básicos), cama/carpa (alojamiento temporal) = supporting en arco alrededor de la casa · fila de 4 chips (Vivienda activo) · retícula = background

Adapt: misma plantilla común de RUBRO; firma: los símbolos se ensamblan alrededor de la casa al nombrarse.
Scene 1 (0.0–0.9s): píldora, título "VIVIENDA", tarjeta; la casa se dibuja (svg self-draw) en el centro de la tarjeta; chip Vivienda verde.
Scene 2 (0.9–3.4s): en "alquiler" (≈1.4s) una llave aparece a la izquierda de la casa; en "servicios básicos" (≈2.2s) un foco y un grifo aparecen arriba-derecha, con línea punteada hacia la casa.
Scene 3 (3.4–5.3s): en "alojamiento temporal" (≈4.0s) una cama sencilla bajo techo aparece a la derecha, unida por una flecha punteada suave desde la casa.
Scene 4 (5.3–7.3s): el subtítulo "Un lugar seguro para tu familia" entra; un escudo/corazón pequeño verde se ilumina sobre la casa; hold quieto.

## Frame 6 — Transporte

- scene: Misma plantilla de rubro: un autobús y un auto avanzan por una ruta punteada hacia un centro de salud y un punto de encuentro. Indicador 2×2 con transporte activo.
- voiceover: "En transporte, calcula pasajes o combustible para traslados esenciales y una salida segura, siguiendo las indicaciones de las autoridades."
- duration: 9.32s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/06-transporte.html
- type: feature_showcase
- persuasion: Concretization
- beat: preparación
- on_screen: "TRANSPORTE" / "Traslados esenciales y salida segura"

narrativeRole: Cuarto rubro esencial, mismo peso visual.
keyMessage: Prever pasajes o combustible para traslados esenciales.

- blueprint: compose
- focal: tarjeta-ilustración de transporte (ruta segura)
- roles: ruta punteada verde, autobús y auto = foreground subject · centro de salud (cruz verde) y punto de encuentro (ícono de personas reunidas en un círculo) como destinos = supporting · fila de 4 chips (Transporte activo) · retícula = background

Compose: misma plantilla común de RUBRO; la ruta se dibuja (svg self-draw) y los vehículos avanzan por ella (motion path suave, power2.inOut).
Scene 1 (0.0–1.0s): píldora, título "TRANSPORTE", tarjeta con un camino curvo (en S) gris claro; chip Transporte verde.
Scene 2 (1.0–3.1s): en "pasajes" (≈1.5s) un ticket pequeño aparece; en "combustible" (≈2.2s) una gota de combustible; el autobús entra por el inicio del camino.
Scene 3 (3.1–6.2s): en "traslados esenciales" la ruta se dibuja en verde punteado; el autobús avanza al centro de salud (destino 1); en "salida segura" el auto avanza al punto de encuentro (destino 2). Subtítulo "Traslados esenciales y salida segura" entra en 3.1s.
Scene 4 (6.2–9.3s): en "indicaciones de las autoridades" una señal informativa azul (flecha) aparece junto a la ruta; hold, solo ruedas girando lento.

## Frame 7 — Ajusta y reserva

- scene: Los cuatro rubros, en tarjetas idénticas, se reúnen alrededor de la libreta del presupuesto familiar (sin porcentajes ni orden de prioridad); debajo aparece una alcancía/frasco pequeño que se llena poco a poco.
- voiceover: "Ajusta los montos a tu realidad y, si puedes, separa una pequeña reserva para imprevistos."
- duration: 6.14s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-ajusta-reserva.html
- type: benefit_highlight
- persuasion: Synthesis (los cuatro rubros juntos, igual tamaño)
- beat: confianza
- on_screen: "Ajusta según tus necesidades" / "Separa una reserva, si puedes"

narrativeRole: Une los cuatro rubros y deja claro que la prioridad la define cada familia.
keyMessage: Los montos se ajustan a cada realidad; una pequeña reserva ayuda.

- blueprint: constellation-hub (Adapt)
- focal: la libreta del presupuesto familiar al centro
- roles: libreta central = foreground subject · cuatro tarjetas de rubro IDÉNTICAS (mismo tamaño, misma distancia al centro, en cuadrícula 2×2 simétrica) = supporting · frasco de reserva = secondary focal · retícula = background

Adapt: los nodos se reúnen alrededor de un centro (cluster→outward expansion invertido: entran desde fuera y se asientan en 2×2 simétrico); sin rotación para no sugerir jerarquía.
Scene 1 (0.0–1.9s): la libreta "Presupuesto familiar" aparece en el centro (y≈640–900); en "ajusta los montos" las cuatro tarjetas (Alimentación, Salud, Vivienda, Transporte, ícono + nombre) llegan simultáneamente desde las cuatro esquinas y se asientan en 2×2 alrededor (y≈380–1160), unidas al centro por líneas punteadas verdes. El título "Ajusta según tus necesidades" (display 700 ~84px) entra arriba en y≈220.
Scene 2 (1.9–2.7s): en "realidad" pequeños controles deslizantes (sin números) bajo cada tarjeta se mueven levemente, cada uno a una posición distinta — sugieren que cada familia ajusta.
Scene 3 (2.7–6.1s): en "separa" (≈2.7s) un frasco de vidrio con etiqueta "Reserva" aparece bajo la cuadrícula (y≈1220–1520); en "pequeña reserva" monedas verdes caen una a una y el nivel sube gradualmente (stat-bars-and-fills, sin números). El subtítulo "Separa una reserva, si puedes" aparece junto al frasco en 2.7s. Hold.

## Frame 8 — Cierre

- scene: La familia cierra la libreta, satisfecha; fondo azul oscuro limpio con las dos frases y un espacio vacío reservado para el logo institucional.
- voiceover: "Planifica hoy. Protege lo esencial y cuida a quienes más quieres."
- duration: 4.67s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-cierre.html
- type: cta
- persuasion: Call to act (tríada breve)
- beat: calidez y esperanza
- on_screen: "Planifica hoy." / "Protege lo esencial."

narrativeRole: Cierra con la acción concreta y deja lugar para la marca institucional.
keyMessage: Planificar hoy protege lo esencial.

- blueprint: titlecard-reveal (Reproduce)
- focal: las dos frases de cierre
- roles: fondo azul oscuro #0B2545 = background (full-bleed) · familia pequeña cerrando la libreta = supporting · rectángulo de espacio para logo (vacío, sin borde visible o con borde punteado blanco al 15 %) = reserved

Scene 1 (0.0–1.1s): fondo azul oscuro; la familia (versión blanca de línea, ~30 % del alto, y≈380–820) cierra la libreta con un check verde. "Planifica hoy." (display 700 ~120px, blanco) entra con slide-up crossfade en y≈960.
Scene 2 (1.1–4.7s): en "protege lo esencial" (≈1.1s) "Protege lo esencial." entra debajo (display 700 ~120px, verde #2BA84A) en y≈1110; una línea verde fina se dibuja bajo ambas frases. Espacio vacío para el logo institucional reservado en y≈1300–1520 (zona libre, 600×220px, centrada). Hold quieto hasta el final, fade a azul en los últimos 0.4s.
