from time import sleep
import RPi.GPIO as GPIO

def set_up_gpio(cruzamento):
    GPIO.setup(cruzamento['semaforo_verde1'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo_amrelo1'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo_vermelho1'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo_verde2'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo_amrelo2'], GPIO.OUT)
    GPIO.setup(cruzamento['semaforo_vermelho2'], GPIO.OUT)


    GPIO.setup(cruzamento['botao_pedestre1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['botao_pedestre2'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_passagem1'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_passagem2'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(cruzamento['sensor_velocidade_1a'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(cruzamento['sensor_velocidade_1b'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(cruzamento['sensor_velocidade_2a'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(cruzamento['sensor_velocidade_2b'], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def fechar_semaforo(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.HIGH)

    # via aux
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.HIGH)

def abrir_via_principal(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.LOW)

    # via aux
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.HIGH)

def alertar_via_principal(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.LOW)

    # via aux
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.HIGH)

def abrir_via_aux(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.HIGH)

    # via aux
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.LOW)

def alertar_via_aux(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.HIGH)

    # via aux
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.LOW)

def modo_noturno(cruzamento):
    # via principal
    GPIO.output(cruzamento['semaforo_verde2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho2'], GPIO.LOW)

    # via aux
    GPIO.output(cruzamento['semaforo_verde1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.LOW)
    GPIO.output(cruzamento['semaforo_vermelho1'], GPIO.LOW)

    sleep(1)
    GPIO.output(cruzamento['semaforo_amrelo1'], GPIO.HIGH)
    GPIO.output(cruzamento['semaforo_amrelo2'], GPIO.HIGH)
    sleep(1)

def iniciar_semaforo(cruzamento):
    GPIO.setmode(GPIO.BCM)
    set_up_gpio(cruzamento)