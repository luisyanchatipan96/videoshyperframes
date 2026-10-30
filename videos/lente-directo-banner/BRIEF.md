---
workflow: product-launch-video
flow: automation
storyboard: yes
message: "Suscríbete a Lente Directo en Facebook por US$2,99 al mes: contenido exclusivo, videos en vivo e insignia de suscriptor."
destination: facebook-banner
aspect: 1920x175
language: es
audience: "Seguidores de la página de Facebook Lente Directo"
length: 30s
angle: cta-promo
narration: yes
vo_mode: restructured
capture: none
---

## Intent

Banner animado profesional de 20 s, 1920×175 px exactos, para promocionar la suscripción
pagada a la página de Facebook «Lente Directo». Estética de medio digital moderno: azul Facebook,
blanco y detalles sutiles en azul oscuro. Limpio, dinámico y legible en pantallas pequeñas.
Símbolo de Facebook y un botón destacado «Suscribirte». Transiciones fluidas, brillos sutiles,
desplazamientos y entradas con profundidad, sin saturar.

## Assets

- capture/assets/logo-lente-directo-blanco.png — logo blanco (principal sobre fondo oscuro).
- capture/assets/logo-lente-directo-color.png — logo en insignia color (alternativo).

## Customizations

- Locución en español latinoamericano, clara, cercana y profesional (ElevenLabs).
- Música moderna, inspiradora y enérgica, a volumen bajo bajo la voz (ElevenLabs Music).
- Efectos de sonido suaves en entradas de texto y en la aparición del botón (ElevenLabs SFX).

## Notes

- Guion ampliado a 30 s con la información real de la página de suscripción (captura del usuario): US$2,99 al mes, cancela cuando quieras, contenido exclusivo, videos en vivo, insignia de suscriptor, «Queremos llevarte la mejor transmisión».
- Botón «Suscribirte» con el icono de insignia turquesa (#14B798) de Facebook.

- No inventar beneficios ni agregar textos pequeños ilegibles.
- Textos, logo e iconos dentro de márgenes seguros.
- Secuencia, textos en pantalla y locución literales del usuario (ver user_script.txt).
- Fondo del banner: #e2b176 (pedido del usuario). Uso: overlay en vivo en OBS.
- Textos en negro y blanco (sin azul), pedido del usuario; azul Facebook solo en el símbolo y el botón.
- Escena 2: texto «En Lente Directo crecemos junto a ti» (pedido del usuario).
- El render sale a 1920×176 (altura par del códec); se recorta a 1920×175 exactos al exportar.
