 Wifi-Cracking 

![Captura de pantalla 2024-07-14 142044](https://github.com/user-attachments/assets/665fbe96-112d-499c-b97b-4d506484b00e)

**Wifi-Cracking** es una herramienta para realizar pruebas de penetración en redes inalámbricas, utilizando herramientas de la suite `aircrack-ng` como `airodump-ng`, `aireplay-ng` y `aircrack-ng`. Esta herramienta está diseñada para facilitar la auditoría de redes Wi-Fi mediante varias funcionalidades automatizadas.

---

## 📋 Requisitos

Para usar esta herramienta, asegúrate de tener instaladas las siguientes dependencias:

- **airodump-ng**
- **aireplay-ng**
- **aircrack-ng**

> **Nota**: Estas herramientas son parte de la suite `aircrack-ng`, disponible para sistemas Unix/Linux.

---

## ⚙️ Funcionalidades

1. **Establecer Modo Monitor**  
   Configura una interfaz de red en modo monitor para realizar actividades de monitoreo y análisis de tráfico de red.

2. **Escanear Redes**  
   Realiza un escaneo de redes en el área utilizando `airodump-ng`, mostrando información detallada sobre cada red detectada.

3. **Capturar Paquetes**  
   Permite capturar paquetes de una red específica y guardar los datos en archivos CSV para su posterior análisis.

4. **Desautenticar Cliente**  
   Envía paquetes de desautenticación a un cliente específico en la red objetivo, permitiendo configurar el número de paquetes y la frecuencia del ataque.

5. **Crackear Contraseña**  
   Usa `aircrack-ng` para intentar crackear la contraseña de una red Wi-Fi protegida con WPA/WPA2. Soporta el uso de diccionarios personalizados.

---

## 🛠️ Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/simoncherry9/wifi-cracking
2. Navega hasta el directorio del proyecto:
   ```bash
   cd wifi-cracking
3. Ejecuta el script principal:
   ```bash
   sudo python3 wifi-cracking.py
4. Sigue las instrucciones en pantalla para usar las diferentes funciones de la herramienta.

---

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, haz un fork y envía un pull request. Asegúrate de incluir pruebas para cualquier cambio importante.

---

## 👤 Autor
Este proyecto fue desarrollado por Saimonch16.

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## ⚠️ Advertencia
La herramienta fue desarrollada con fines educativos y de auditoría ética. No me hago responsable por el mal uso que se le pueda dar. Utilízala solo en redes en las que tengas permiso para realizar pruebas de penetración.
