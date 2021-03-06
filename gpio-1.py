import RPi.GPIO as GPIO
import time

btnPin=13
ledPin=7
ledOn = False
counter = 0
limit = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(btnPin,GPIO.IN)
while True:
    btnPressed = not GPIO.input(btnPin)
    if btnPressed: 
        ledOn = not ledOn
        GPIO.output(ledPin,ledOn)
        counter += 1
        time.sleep(1)
        if counter >= limit: break
        print('btnPressed',counter,ledOn)
GPIO.output(ledPin,False)
GPIO.cleanup()