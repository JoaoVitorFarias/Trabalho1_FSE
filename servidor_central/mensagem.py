import socket_central

monitoramento_acionado = False

def enviar_mensagem(modo_noturno, modo_emergencia, opcao):
    msg = {
        'modo_noturno': int(modo_noturno),
        'modo_emergencia': int(modo_emergencia)
    }

    if(opcao == 1):
        socket_central.enviar_msg(msg, socket_central.socket_conexao1)
        socket_central.enviar_msg(msg, socket_central.socket_conexao2)
        socket_central.enviar_msg(msg, socket_central.socket_conexao3)
        socket_central.enviar_msg(msg, socket_central.socket_conexao4)
    
    elif(opcao == 2):
        socket_central.enviar_msg(msg, socket_central.socket_conexao1)
        socket_central.enviar_msg(msg, socket_central.socket_conexao2)
    
    elif(opcao == 3):
        socket_central.enviar_msg(msg, socket_central.socket_conexao3)
        socket_central.enviar_msg(msg, socket_central.socket_conexao4)

def imprimir_mensagem(msg):
    if ((msg['tipo'] == 1) 
        and monitoramento_acionado):
        print("[QNT_CARROS] Via principal: " + str(msg['qnt_carros_principal']) + 
                "\n[QNT_CARROS] Via auxiliar: " + str(msg['qnt_carros_aux']) +
                "\nVelocidade média: " + str(msg['velocidade_media']) + "km/h\n")
    
    if ((msg['tipo'] == 2) 
        and monitoramento_acionado):
        print("[INFRACAO] Ultrapassou o limite de velocidade: " + str(msg['infracao_velocidade']) + "\n")

    if ((msg['tipo'] == 3) 
        and monitoramento_acionado):
        print("[INFRACAO] Ultrapassou o semáforo vermelho: " + str(msg['infracao_semaforo']) + "\n")



def acionar_monitoramento(opcao):
    global monitoramento_acionado

    if(opcao == 1):
        monitoramento_acionado = True
    else:
        monitoramento_acionado = False
