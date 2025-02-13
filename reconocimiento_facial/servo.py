import RPi.GPIO as GPIO
import time
def AngleToDuty(ang):
    return float(pos)/10.+5.
  
#Setup servoPin as PWM output of frequancy 100Hz
servoPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin,100)
#setup sweep parameters
depart =0
arrivee=180
DELAY=0.1
incStep=5
pos=depart

if __name__ == '__main__' :
    pwm.start(AngleToDuty(pos)) #star pwm
    nbRun=3
    i=0
    while i<nbRun:
        print("--------------------------run {}".format(i)) 
        for pos in range(depart,arrivee,incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
        print("position: {}° -> duty cycle : {}%".format(pos,duty))
        
        for pos in range(arrivee,depart,-incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            time.sleep(DELAY)
        print("position: {}° -> duty cycle : {}%".format(pos,duty))
        
        i=i+1
      
    pwm.stop() #stop sending value to output
    GPIO.cleanup() #release channel