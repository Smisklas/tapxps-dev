import RPi.GPIO as GPIO
from time import sleep, ctime, time
from threading import Thread
from gpiozero import PWMOutputDevice

class Pin():
    # This class controls the the output of one pin with the on off methods.
    def __init__(self,pin_number):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT)
        GPIO.output(self.pin_number, 0)
    def on(self):
        GPIO.output(self.pin_number,1)
    def off(self):
        GPIO.output(self.pin_number,0)
    def trigger(self, action_time):
        GPIO.output(self.pin_number,1)
        sleep(action_time/1000)
        GPIO.output(self.pin_number,0)


class Valve(Pin):
    # class to handle valves
    def __init__(self, pin_number, name):
        super().__init__(pin_number)
        self.name = name
        self.status = 'Closed'

    def open(self):
        GPIO.output(self.pin_number,1)
        print('{} opened.'.format(self.name))
        self.update_status()


    def close(self):
        GPIO.output(self.pin_number,0)
        print('{} closed.'.format(self.name))
        self.update_status()

    def update_status(self):
        status = GPIO.input(self.pin_number)
        if status == 0:
            self.status = 'Closed'
        elif status == 1:
            self.status =  'Open'
        else:
            self.status = 'Error'

class Injector(Pin):
    #Class to handle an injector 
    def __init__(self, pin_number, name):
        super().__init__(pin_number)
        self.name = name

    def run(self,action_time, delay):
        sleep(delay)
        GPIO.output(self.pin_number, 1)
        print('{}: {} triggered'.format(ctime(time()), self.name))
        sleep(action_time)
        GPIO.output(self.pin_number, 0)


class Measurement(Pin):
    #class to handle the measurement with a single trigger.
    def __init__(self, pins):
        self.channels = [Pin(pin) for pin in pins]
    
    def run(self, time, rest):
        print('tester')
        threads = [Thread(target=channel.trigger, args=(10,)) for channel in self.channels]
        threads.append(Thread(target = sleep, args = (time,)))
        for thread in threads:
            thread.start()
        sleep(rest)

class pwmTrigger(PWMOutputDevice):
    def __init__(self, pin):
        super().__init__(pin)
        self.aq_time = 0
        self.frequency = 1
        self.value = 1
    def run(self, time):
        print('PWM on')
        self.value = 0.5
        sleep(time)
        self.value = 1
        print('PWM off')



class sleeper():
    def __init__(self):
        pass
    def run(self, time):
        sleep(time)

def cycle(objlist, trigger):
    for _ in range(1000):
        for object in objlist:
            object.trigger(trigger)
        sleep(1)
# For testing classes to be usesd with the RPi

if __name__=='__main__':
    WATERPIN = 17
    PREPIN = 27
    GPIO.setmode(GPIO.BCM)
    water = Pin(WATERPIN)
    pre = Pin(PREPIN)

