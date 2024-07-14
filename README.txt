==============================================================
          Herramienta de Seguridad Wi-Fi - Documentación
==============================================================

Este repositorio contiene una herramienta de seguridad Wi-Fi diseñada para realizar diversas acciones relacionadas con pruebas de penetraciòn en redes inalámbricas utilizando herramientas populares como `airodump-ng`, `aireplay-ng` y `aircrack-ng`.

Requisitos:
-----------
Para utilizar esta herramienta, asegúrate de tener instaladas las siguientes dependencias:

- `airodump-ng`
- `aireplay-ng`
- `aircrack-ng`

Estas herramientas están disponibles como parte de la suite `aircrack-ng`, que puede ser instalada en sistemas Unix/Linux.

Funcionalidades:
----------------
1. Establecer Modo Monitor: Permite configurar una interfaz de red específica en modo monitor para realizar actividades de monitoreo y análisis.

2. Escanear Redes: Realiza un escaneo de redes disponibles en el área utilizando `airodump-ng`, mostrando información detallada sobre cada red encontrada.

3. Capturar Paquetes: Permite capturar paquetes de una red específica utilizando `airodump-ng`. Los datos capturados se guardan en archivos CSV para su posterior análisis.

4. Desautenticar Cliente: Envía paquetes de desautenticación a un cliente específico de una red Wi-Fi objetivo. Puedes elegir la cantidad de paquetes a enviar y tienes la opción de repetir el ataque.

5. Crackear Contraseña: Utiliza `aircrack-ng` para intentar crackear la contraseña de una red Wi-Fi protegida con cifrado WPA/WPA2. Puedes usar un diccionario por defecto o especificar uno personalizado.

Uso:
----
1. Clona este repositorio en tu máquina local

2. Navega hasta el directorio del proyecto:
$ cd wifi-cracking

3. Ejecuta el script principal:
$ sudo python wifi-cracking.py o 
$ sudo python3 wifi-cracking.py


4. Sigue las instrucciones en pantalla para utilizar las diferentes funciones de la herramienta.

Contribuciones:
---------------
Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar pull requests con tus mejoras. Asegúrate de incluir pruebas para cualquier cambio significativo.

Autor:
------
Este proyecto fue desarrollado por Saimonch16(https://github.com/simoncherry9).

Licencia:
---------
Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.
