import socket
import json
import mensagem
from time import sleep

socket_cruzamento1 = None
socket_cruzamento2 = None

def monitorar_socket(socket):
    while True:
        data = socket.recv(1024).decode('utf-8')
        msg = json.loads(data)   

        mensagem.verificar_mensagem(msg)
        sleep(1)

def iniciar_socket(host, port, id_cruzamento):
    try:
        if(id_cruzamento == 1):
            global socket_cruzamento1
            socket_cruzamento1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento1.connect((host, port))

            monitorar_socket(socket_cruzamento1)

        if(id_cruzamento == 2):
            global socket_cruzamento2
            socket_cruzamento2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento2.connect((host, port))

            monitorar_socket(socket_cruzamento2)
    except:
        print("socket error - conexão")


def enviar_msg(msg, socket):
    try:
        socket.send(bytes((json.dumps(msg)),encoding="utf-8"))
        sleep(1)
    except:
        print("socket error - envio de mensagem")
        