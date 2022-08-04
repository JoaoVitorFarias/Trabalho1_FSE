from multiprocessing import connection
import socket
import threading
import json
import cruzamento
import socket_distribuido
import sys

# cruzamentos
cruzamento1 ={
    'semaforo_verde1': 1,
    'semaforo_amrelo1': 26,
    'semaforo_vermelho1': 21,
    'semaforo_verde2': 20,
    'semaforo_amrelo2': 16,
    'semaforo_vermelho2': 12,
    'botao_pedestre1': 8,
    'botao_pedestre2': 7,
    'sensor_passagem1': 14,
    'sensor_passagem2': 15,
    'sensor_velocidade_1a': 18,
    'sensor_velocidade_1b': 23,
    'sensor_velocidade_2a': 24,
    'sensor_velocidade_2b': 25
}

cruzamento2 ={
    'semaforo_verde1': 2,
    'semaforo_amrelo1': 3,
    'semaforo_vermelho1': 11,
    'semaforo_verde2': 0,
    'semaforo_amrelo2': 5,
    'semaforo_vermelho2': 6,
    'botao_pedestre1': 10,
    'botao_pedestre2': 9,
    'sensor_passagem1': 4,
    'sensor_passagem2': 17,
    'sensor_velocidade_1a': 27,
    'sensor_velocidade_1b': 22,
    'sensor_velocidade_2a': 13,
    'sensor_velocidade_2b': 19
}

def enviar_msg(msg):
    global socket_distr
    socket_distr.sendall(bytes((json.dumps(msg)),encoding="utf-8"))

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Informe o host e as portas para cada cuzamento\n")
        print("python msin.py <HOST> <PORTA_PRIMEIRO_CRUZAMENTO> <PORTA_SEGUNDO_CRUZAMENTO>\n")
        sys.exit()

    thread_socket1 = threading.Thread(target=socket_distribuido.iniciar_socket, args=(sys.argv[1], int(sys.argv[2]), 1))
    thread_socket2 = threading.Thread(target=socket_distribuido.iniciar_socket, args=(sys.argv[1], int(sys.argv[3]), 2))

    thread_cruzamento1 = threading.Thread(target=cruzamento.iniciar_controle_cruzamento, args=(cruzamento1,))
    thread_cruzamento2 = threading.Thread(target=cruzamento.iniciar_controle_cruzamento, args=(cruzamento2,))
    
    thread_socket1.start()
    thread_socket2.start()
    thread_cruzamento1.start()
    thread_cruzamento2.start()
    