# Frame packet: 06-transporte

## Project inputs

- Project: /home/user/videos/presupuesto-emergencia-el-nino
- Design tokens: /home/user/videos/presupuesto-emergencia-el-nino/frame.md
- RULES_DIR: /home/user/.agents/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 6 — Transporte

- scene: Misma plantilla de rubro: un autobús y un auto avanzan por una ruta punteada hacia un centro de salud y un punto de encuentro. Indicador 2×2 con transporte activo.
- voiceover: "En transporte, calcula pasajes o combustible para traslados esenciales y una salida segura, siguiendo las indicaciones de las autoridades."
- duration: 9.32s
- transition_in: push-slide LEFT
- status: outline
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
