import socket
import json
import mensagem
from time import sleep

socket_cruzamento1 = None
socket_cruzamento2 = None

socket_cruzamento3 = None
socket_cruzamento4 = None

socket_conexao1 = None
socket_conexao2 = None

socket_conexao3 = None
socket_conexao4 = None

'''
def monitorar_socket(socket):
    while True:
        conn, addr = socket.accept()
        conexao = conn

        while True:
            data = conexao.recv(1024).decode('utf-8')
            msg = json.loads(data) 

            mensagem.imprimir_mensagem(msg)
            sleep(1)
'''

def iniciar_socket(host, port, id_cruzamento):
    try:
        if(id_cruzamento == 1):
            global socket_cruzamento1
            socket_cruzamento1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento1.bind((host, port))
            socket_cruzamento1.listen()

            while True:
                global socket_conexao1
                conn, addr = socket_cruzamento1.accept()
                socket_conexao1 = conn

                while True:
                    data = socket_conexao1.recv(1024).decode('utf-8')
                    msg = json.loads(data) 

                    mensagem.imprimir_mensagem(msg)
                    sleep(1)

        if(id_cruzamento == 2):
            global socket_cruzamento2
            socket_cruzamento2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento2.bind((host, port))
            socket_cruzamento2.listen()

            while True:
                global socket_conexao2
                conn, addr = socket_cruzamento2.accept()
                socket_conexao2 = conn

                while True:
                    data = socket_conexao2.recv(1024).decode('utf-8')
                    msg = json.loads(data) 

                    mensagem.imprimir_mensagem(msg)
                    sleep(1)

        if(id_cruzamento == 3):
            global socket_cruzamento3
            socket_cruzamento3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento3.bind((host, port))
            socket_cruzamento3.listen()

            while True:
                global socket_conexao3
                conn, addr = socket_cruzamento3.accept()
                socket_conexao3 = conn

                while True:
                    data = socket_conexao3.recv(1024).decode('utf-8')
                    msg = json.loads(data) 

                    mensagem.imprimir_mensagem(msg)
                    sleep(1)

        if(id_cruzamento == 4):
            global socket_cruzamento4
            socket_cruzamento4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_cruzamento4.bind((host, port))
            socket_cruzamento4.listen()

            while True:
                global socket_conexao4
                conn, addr = socket_cruzamento4.accept()
                socket_conexao4 = conn

                while True:
                    data = socket_conexao4.recv(1024).decode('utf-8')
                    msg = json.loads(data) 

                    mensagem.imprimir_mensagem(msg)
                    sleep(1)
    except:
        print("socket error - conexão")


def enviar_msg(msg, socket):
    try:
        socket.send(bytes((json.dumps(msg)),encoding="utf-8"))
        sleep(1)
    except:
        print("socket error - envio de mensagem")