import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 21
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
#print("Calibrating.....")
time.sleep(2)

#print ("Place the object......")

def check_for_car():
        try:
                while True:
                        # Send a short ultrasound pulse
                   GPIO.output(TRIG, True)
                   print('start')
                   time.sleep(0.00001)
                   GPIO.output(TRIG, False)

                        #listen for echo
                   while GPIO.input(ECHO)==0:
                          pulse_start = time.time()

                   while GPIO.input(ECHO)==1:
                          pulse_end = time.time()

                        # calculate distance
                   pulse_duration = pulse_end - pulse_start

                   distance = pulse_duration * 17150

                   distance = round(distance+1.15, 2)
                   
                   # return if there is an object in range of 100cm
                   if distance <= 100:
                       #print(distance)
                       return True
                   else:
                           return False

        except KeyboardInterrupt:
                GPIO.cleanup()

#occupied = check_for_car()
#print(occupied)

