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

StartTime = time.time()
fpsFilter = 0
MaxRate = 5000
FrameRate = MaxRate
FrameNum = 0

while True:
    FrameNum += 1
    btnPressed = not GPIO.input(btnPin)
    if btnPressed: 
        ledOn = not ledOn
        GPIO.output(ledPin,ledOn)
        counter += 1
        time.sleep(1)
        if counter >= limit: break
        print('btnPressed',counter,ledOn)
    dt = time.time() - StartTime
    fps = 1/dt
    fpsFilter = 0.95*fpsFilter + 0.05*fps
    StartTime = time.time()
    title = str(round(fpsFilter,1)) + ' fps '
    print(title)
GPIO.output(ledPin,False)
GPIO.cleanup()