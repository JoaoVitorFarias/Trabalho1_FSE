import RPi.GPIO as GPIO

def verificar_botao_acionado(botao):
    if GPIO.event_detected(botao):
        GPIO.remove_event_detect(botao)
        GPIO.add_event_detect(botao, GPIO.RISING, bouncetime=300)
        return True
    return False

def iniciar_botao(botao):
    GPIO.add_event_detect(botao, GPIO.RISING, bouncetime=300)

