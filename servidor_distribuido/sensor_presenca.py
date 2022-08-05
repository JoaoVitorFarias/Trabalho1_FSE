import RPi._GPIO as GPIO

def verificar_carro(sensor):
    if GPIO.event_detected(sensor):
        GPIO.remove_event_detect(sensor)
        GPIO.add_event_detect(sensor, GPIO.RISING, bouncetime=100)
        return True
    return False

def iniciar_sensor_presenca(sensor):
    GPIO.add_event_detect(sensor, GPIO.RISING, bouncetime=100)
