## Video direction

- canvas: banner 1920×175 px (franja horizontal para OBS). Fondo #e2b176 con un brillo radial más claro al centro (#EDC28C) y bordes algo más oscuros (#D7A367), siempre en su propio clip de fondo.
- layout fijo (igual en todas las escenas, como en los bocetos confirmados): logo blanco a la izquierda (x 120, alto 135), divisor fino oscuro en x 285, texto central entre x 330 y 1530, zona derecha x 1440–1800 para el símbolo de Facebook y/o el botón «Suscribirte» (azul #1877F2 con la insignia turquesa #14B798). Márgenes seguros: x ≥ 110 y ≤ 1810, y 14–161.
- type: Poppins (assets/fonts/Poppins_400…800.woff2). Texto principal negro #141414; palabras destacadas en blanco con sombra suave. Sin azul en los textos.
- motion grammar: entradas con profundidad — desenfoque que se aclara (blur 12px→0) + opacidad + desplazamiento corto (x 40px o y 24px) + escala 0.96→1, curvas largas sin rebote (power3.out / expo.out). Brillos sutiles: un barrido de luz blanca diagonal (shimmer) una sola vez sobre el elemento clave. Nada de rebotes exagerados ni "respiración" constante; el único latido permitido es el pulso del botón en las escenas 5 y 6 (2 pulsos suaves 1→1.05→1, no infinito).
- continuidad: el logo y el divisor están en la misma posición en todas las escenas. En la escena 1 el logo entra; en las escenas 2–6 ya está presente desde t=0 (sin re-entrada) para que el corte entre escenas no lo haga parpadear.
- audio: la locución, la música y los efectos los coloca el orquestador en la raíz; ningún elemento de audio dentro de los frames.
- negative list: no textos pequeños ilegibles (mínimo 32 px), no beneficios inventados, no saturar con partículas, no rebotes, ni slideshow (todo en t=0 y congelado) ni salvapantallas.

