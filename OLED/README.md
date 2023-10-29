# Juego Triqui con ESP32 y MicroPython 🎮


¡Bienvenido al emocionante mundo del Triqui! 🎮 En este proyecto, te presento una implementación única del clásico juego de tres en raya utilizando una ESP32 y el poderoso lenguaje de programación MicroPython.🚀 Prepárate para sumergirte en una experiencia de juego interactiva y adictiva. 😃

<p align="center">
  <img src="https://github.com/david0-012/ESP32-MicroPython/assets/84252258/643c02d6-adfa-4d21-9120-fb8f68707719" width="500" alt="WhatsApp Image 2023-10-29 at 12:44:12 AM" style="display: block; margin: 0 auto;">
</p>

## Características Principales

- 💡 MicroPython: Aprovechamos las ventajas de este lenguaje de programación eficiente y fácil de aprender para dar vida al juego Triqui.
- 📟 ESP32: Utilizamos esta increíble placa de desarrollo que ofrece una amplia gama de posibilidades y un rendimiento excepcional.
- 🖥️ Pantalla OLED: Disfruta de una experiencia visual impresionante gracias a la pantalla OLED que muestra el tablero y los movimientos de los jugadores.
- 🕹️ Joystick: ¡Controla la acción con un joystick! Utiliza su intuitivo control para seleccionar la posición donde deseas colocar tu X o círculo.
- ✔️ Botón de confirmación: Una vez que hayas decidido tu jugada, simplemente presiona el botón para confirmar y colocar tu símbolo en el tablero.
- 🏆 Detección de victoria y empate para mantener el juego emocionante.
- 🎨 Personaliza tus propias reglas de Triqui modificando el código.

## Requisitos

Para disfrutar de este juego, necesitarás:

- 📟 Una placa de desarrollo ESP32.
- 💡 MicroPython instalado en la ESP32.
- 📺 Una pantalla OLED compatible con el controlador SSD1306.
- 🎮 Un joystick para un control táctil.
- 🛡️ Un botón de confirmación para realizar tus movimientos con estilo.
- 🧰 Conexiones de protoboard para mantener todo en su lugar.

## Conexiones

Asegúrate de que las conexiones de hardware se realicen de la siguiente manera:

- **Pantalla OLED:**
  - VCC ➡️ 3.3V
  - GND ➡️ GND
  - SDA ➡️ Pin I2C SDA en la ESP32 (por defecto, Pin 23)
  - SCL ➡️ Pin I2C SCL en la ESP32 (por defecto, Pin 22)

- **Joystick:**
  - Eje X ➡️ Pin Analógico en la ESP32 (por ejemplo, Pin 34)
  - Eje Y ➡️ Pin Analógico en la ESP32 (por ejemplo, Pin 35)
  - Botón del Joystick ➡️ Pin digital en la ESP32 (por ejemplo, Pin 21)
  - GND ➡️ GND
  - VCC ➡️ 3.3V

- **Botón de Confirmación:**
  - Uno de los terminales del botón (GND) ➡️ GND
  - Otro terminal del botón (VCC) ➡️ 3.3V
  - El tercer terminal del botón (pin) ➡️ Pin digital en la ESP32 (por ejemplo, Pin 19)

Asegúrate de que las conexiones coincidan con los pines especificados en el código o modifica el código para que refleje las conexiones adecuadas.

## Instalación

1. 📥 Clona este repositorio en tu máquina local.
2. 💾 Copia el archivo `sdd1306.py` en tu ESP32.
3. 🔌 Conecta la pantalla OLED y el joystick a la ESP32 siguiendo las especificaciones de hardware.
4. ⚙️ Carga el archivo `TRIQUI.py` en tu ESP32 utilizando tu entorno de desarrollo preferido.

## ¡A Jugar!

1. 💡 Enciende la ESP32 y espera a que se inicie.
2. 🎮 El juego Triqui se mostrará en la pantalla OLED, listo para que demuestres tus habilidades.
3. 🕹️ Utiliza el joystick para mover la selección y el botón de confirmación para colocar tu símbolo.
4. 🔄 ¡Sigue jugando hasta que un jugador logre completar una línea de tres símbolos o se produzca un empate!

## Personalización

Siéntete libre de personalizar las reglas del juego modificando el código fuente. ¡Deja volar tu creatividad! Cambia el aspecto, las condiciones de victoria o cualquier otro aspecto del Triqui a tu gusto.

## Contribuye al Proyecto

Si te encanta el Triqui tanto como a nosotros y quieres aportar tu granito de arena, ¡te damos la bienvenida a nuestra comunidad de desarrolladores! 🤝

1. 🍴 Haz un fork de este repositorio para crear tu propia copia.
2. ✨ Crea una rama con el nombre de tu nueva funcionalidad: `git checkout -b mi-nueva-funcionalidad`.
3. 🛠️ Realiza los cambios necesarios y realiza commits descriptivos: `git commit -m "Agrega mi nueva funcionalidad"`.
4. 📤 Envía tus cambios al repositorio remoto: `git push origin mi-nueva-funcionalidad`.
5. 📩 Abre un Pull Request en GitHub y describe detalladamente los cambios que realizaste. ¡Estaremos encantados de revisarlo!

## Contacto

Si tienes alguna pregunta, comentario o simplemente deseas compartir tu experiencia de juego, no dudes en contactarme a través de [davidcasallas1202@gmail.com]. ¡Esperamos que disfrutes el juego! 🎉
