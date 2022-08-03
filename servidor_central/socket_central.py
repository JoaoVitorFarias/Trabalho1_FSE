import socket
import json
import mensagem

socket_cruzamento1 = None
socket_cruzamento2 = None

socket_cruzamento3 = None
socket_cruzamento4 = None

def monitorar_socket(socket):
    while True:
        conn, addr = socket.accept()
        global conexao
        conexao = conn

        while True:
            data = conexao.recv(1024).decode('utf-8')
            msg = json.loads(data) 

            mensagem.imprimir_mensagem(msg)

def iniciar_socket(host, port, id_cruzamento):
    if(id_cruzamento == 1):
        global socket_cruzamento1
        socket_cruzamento1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cruzamento1.bind((host, port))
        socket_cruzamento1.listen()

        monitorar_socket(socket_cruzamento1)
    
    if(id_cruzamento == 2):
        global socket_cruzamento2
        socket_cruzamento2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cruzamento2.bind((host, port))
        socket_cruzamento2.listen()

        monitorar_socket(socket_cruzamento2)
    
    if(id_cruzamento == 3):
        global socket_cruzamento3
        socket_cruzamento3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cruzamento3.bind((host, port))
        socket_cruzamento3.listen()

        monitorar_socket(socket_cruzamento3)
    
    if(id_cruzamento == 4):
        global socket_cruzamento4
        socket_cruzamento4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cruzamento4.bind((host, port))
        socket_cruzamento4.listen()

        monitorar_socket(socket_cruzamento4)


def enviar_msg(msg, socket):
    socket.sendall(bytes((json.dumps(msg)),encoding="utf-8"))