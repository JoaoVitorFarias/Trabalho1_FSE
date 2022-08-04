from time import sleep
import semaforo
import botao_pedestre
import sensor_presenca
from ControleVelocidade import ControleVelocidade
import sensor_velocidade
import mensagem

modo_noturno = False
modo_emergencia = False

def ativar_modo_noturno(cruzamento):
    while modo_noturno:
        semaforo.modo_noturno(cruzamento)
    
    controlar_semaforo(cruzamento)

def ativar_modo_emergencia(cruzamento):
    while modo_emergencia:
        semaforo.abrir_via_principal(cruzamento)
    
    controlar_semaforo(cruzamento)

def controlar_via_principal(cruzamento):
    semaforo.abrir_via_principal(cruzamento)

    controle_sensor1 = ControleVelocidade(cruzamento['sensor_velocidade_1a'], cruzamento['sensor_velocidade_1b'])
    controle_sensor2 = ControleVelocidade(cruzamento['sensor_velocidade_2a'], cruzamento['sensor_velocidade_2b'])

    tempo_max = 20
    tempo_min = 10
    botao_pressionado = False
    sensor_presenca_acionado = False

    # cronômetro
    while (tempo_max > 0):
        sleep(0.7)
        tempo_max = tempo_max - 1

        if(botao_pedestre.verificar_botao_acionado(cruzamento['botao_pedestre2'])
            and (tempo_max <= tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
            break

        if (botao_pedestre.verificar_botao_acionado(cruzamento['botao_pedestre2'])
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
        
        if ((sensor_presenca.verificar_carro(cruzamento['sensor_passagem1']) 
            or sensor_presenca.verificar_carro(cruzamento['sensor_passagem2']))
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            break

        if ((sensor_presenca.verificar_carro(cruzamento['sensor_passagem1']) 
            or sensor_presenca.verificar_carro(cruzamento['sensor_passagem2']))
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            sensor_presenca_acionado = True

        controle_sensor1.verificar_sensor_velociadade()
        controle_sensor2.verificar_sensor_velociadade()

        if(modo_noturno):
            ativar_modo_noturno(cruzamento)
        
        if(modo_emergencia):
            ativar_modo_emergencia(cruzamento)
        
        
        if((tempo_max % 2) == 0):
            qnt_carros = int(controle_sensor1.qnt_carros + controle_sensor2.qnt_carros)
            if ((controle_sensor1.qnt_carros + controle_sensor2.qnt_carros) == 0):
                velocida_media =0
            else:
                velocida_media = (controle_sensor1.velocidade_total + controle_sensor2.velocidade_total)/(controle_sensor1.qnt_carros + controle_sensor2.qnt_carros)
            mensagem.enviar_mensagem_qnt_carros(qnt_carros, 0, velocida_media, cruzamento)

    semaforo.alertar_via_principal(cruzamento)
    sleep(3)

    qnt_infracao = int(controle_sensor1.qnt_infracao + controle_sensor2.qnt_infracao)
    mensagem.enviar_mensagem_infracao_velocidade(qnt_infracao, cruzamento)


def controlar_via_aux(cruzamento):
    semaforo. abrir_via_aux(cruzamento)

    controle_sensor1 = ControleVelocidade(cruzamento['sensor_velocidade_1a'], cruzamento['sensor_velocidade_1b'])
    controle_sensor2 = ControleVelocidade(cruzamento['sensor_velocidade_2a'], cruzamento['sensor_velocidade_2b'])
    
    tempo_max = 10
    tempo_min = 5
    botao_pressionado = False
    sensor_presenca_acionado = False

    # cronômetro
    while (tempo_max > 0):
        sleep(0.7)
        tempo_max = tempo_max - 1

        if(botao_pedestre.verificar_botao_acionado(cruzamento['botao_pedestre1'])
            and (tempo_max <= tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
            break

        if (botao_pedestre.verificar_botao_acionado(cruzamento['botao_pedestre1'])
            and (tempo_max > tempo_min) 
            and ( not botao_pressionado)):
            botao_pressionado = True
        
        if ((controle_sensor1.verificar_carro_esperando()
            or controle_sensor2.verificar_carro_esperando())
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            break

        if ((controle_sensor1.verificar_carro_esperando()
            or controle_sensor2.verificar_carro_esperando())
            and (tempo_max <= tempo_min) 
            and ( not sensor_presenca_acionado)):
            sensor_presenca_acionado = True
        
        if(sensor_presenca.verificar_carro(cruzamento['sensor_passagem1'])):
            controle_sensor1.adicionar_carro()

        if(sensor_presenca.verificar_carro(cruzamento['sensor_passagem2'])):
            controle_sensor2.adicionar_carro()
        
        if(controle_sensor1.verificar_infracao()):
            controle_sensor1.adicionar_infracao()
        
        if(controle_sensor2.verificar_infracao()):
            controle_sensor2.adicionar_infracao()

        if(modo_noturno):
            ativar_modo_noturno(cruzamento)
        
        if(modo_emergencia):
            ativar_modo_emergencia(cruzamento)

        if((tempo_max % 2) == 0):
            qnt_carros = int(controle_sensor1.qnt_carros + controle_sensor2.qnt_carros)
            mensagem.enviar_mensagem_qnt_carros(0, qnt_carros, 0, cruzamento)

    semaforo.alertar_via_aux(cruzamento)
    sleep(3)

    qnt_infracao = int(controle_sensor1.qnt_infracao + controle_sensor2.qnt_infracao)
    mensagem.enviar_mensagem_infracao_semaforo(qnt_infracao, cruzamento)

def controlar_semaforo(cruzamento):
    while True:
        semaforo.fechar_semaforo(cruzamento)
        sleep(1)
        controlar_via_principal(cruzamento)
        semaforo.fechar_semaforo(cruzamento)
        sleep(1)
        controlar_via_aux(cruzamento)


def iniciar_controle_cruzamento(cruzamento):
    semaforo.iniciar_semaforo(cruzamento)

    botao_pedestre.iniciar_botao(cruzamento['botao_pedestre1'])
    botao_pedestre.iniciar_botao(cruzamento['botao_pedestre2'])
    sensor_presenca.iniciar_sensor_presenca(cruzamento['sensor_passagem1'])
    sensor_presenca.iniciar_sensor_presenca(cruzamento['sensor_passagem2'])
    sensor_velocidade.iniciar_sensor_velocidade(cruzamento['sensor_velocidade_1a'])
    sensor_velocidade.iniciar_sensor_velocidade(cruzamento['sensor_velocidade_1b'])
    sensor_velocidade.iniciar_sensor_velocidade(cruzamento['sensor_velocidade_2a'])
    sensor_velocidade.iniciar_sensor_velocidade(cruzamento['sensor_velocidade_2b'])

    controlar_semaforo(cruzamento)