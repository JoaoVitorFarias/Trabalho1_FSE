import sys
import threading
import socket_central
from Menu import Menu
   
if __name__ == "__main__":

    if len(sys.argv) < 5:
        print("Informe o host e as portas para cada cuzamento\n")
        print("python main.py <HOST> <PORTA_CRUZAMENTO1> <PORTA_CRUZAMENTO2> <PORTA_CRUZAMENTO3> <PORTA_CRUZAMENTO4>\n")
        sys.exit()

    menu = Menu()

    thread_cruzamento1 = threading.Thread(target=socket_central.iniciar_socket, args=(sys.argv[1], int(sys.argv[2]), 1))
    thread_cruzamento2 = threading.Thread(target=socket_central.iniciar_socket, args=(sys.argv[1], int(sys.argv[3]), 2))
    thread_cruzamento3 = threading.Thread(target=socket_central.iniciar_socket, args=(sys.argv[1], int(sys.argv[4]), 3))
    thread_cruzamento4 = threading.Thread(target=socket_central.iniciar_socket, args=(sys.argv[1], int(sys.argv[5]), 4))
    thread_menu = threading.Thread(target=menu.menu_principal)
    
    thread_cruzamento1.start()
    thread_cruzamento2.start()
    thread_cruzamento3.start()
    thread_cruzamento4.start()
    thread_menu.start()
