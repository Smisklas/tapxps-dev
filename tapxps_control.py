import sys
from tapxps_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
import RPi.GPIO as GPIO
from gpio_classes import Pin, Injector, Measurement, pwmTrigger, Valve
from threading import Thread
from time import sleep
        
class QValve(QObject):
    
    action = pyqtSignal()
    
    def __init__(self, device):
        super(QValve, self).__init__()
        self.device = device

    @pyqtSlot()
    def open(self):
        self.device.open()
        self.action.emit()


    @pyqtSlot()
    def close(self):
        self.device.close()
        self.action.emit()



class Main_looper_signals(QObject):
    
    progress = pyqtSignal(int)
    status = pyqtSignal(str)


class Main_looper(QRunnable):
    def __init__(self, wait_time, pulse_time, aq_time, cycles):
        super(Main_looper, self).__init__()
        self.wait_time = wait_time
        self.pulse_time = pulse_time
        self.aq_time = aq_time
        self.pool = QThreadPool()
        self.cycles = cycles
        self.signals = Main_looper_signals()

    def run(self):
        
        self.signals.progress.emit(0)
        

        for cycle in range(1,self.cycles+1):
            pulser = Pulser(self.pulse_time)
            trigger = Trigger(self.aq_time)
            self.signals.status.emit('Triggering')
            pulser.signals.inlet_open.connect(w.inlet.open)
            pulser.signals.inlet_close.connect(w.inlet.close)
            pulser.signals.bypass_open.connect(w.bypass.open)
            pulser.signals.bypass_close.connect(w.bypass.close)
            self.pool.start(pulser)
            self.pool.start(trigger)
            self.pool.waitForDone()
            if cycle < self.cycles:
                self.signals.status.emit('Resting')
                sleep(self.wait_time)
            else:
                pass
            self.signals.progress.emit(int(100*cycle/self.cycles))
        self.signals.status.emit('Done')




class PulserSignals(QObject):

    inlet_open = pyqtSignal()
    inlet_close = pyqtSignal()
    bypass_open = pyqtSignal()
    bypass_close = pyqtSignal()


class Tasker(QObject):

    def __init__(self):
        super(Tasker, self).__init__()
        self.mainpool = QThreadPool()
        self.pool = QThreadPool()
        self.pulse_time = 1
        self.aq_time = 1
        self.cycles = 1
        self.rest_time = 1

    def run(self):
        #for cycle in range(1,self.cycles+1):
         
         t = Main_looper(self.rest_time, self.pulse_time, self.aq_time, self.cycles)
         t.signals.progress.connect(w.ui.progressBar.setValue)
         t.signals.status.connect(w.ui.trigger_status.setText)
         self.pool.start(t)
             
    def update_aq_time(self,value):
        self.aq_time = value

    def update_pulse_time(self, value):
        self.pulse_time = value

    def update_cycles(self, value):
        self.cycles = value

    def update_rest_time(self, value):
        self.rest_time = value

class Pulser(QRunnable):
    # Worker class for pulsing valves
    
    signals = PulserSignals()

    def __init__(self, pulse_time):
        super(Pulser, self).__init__()
        self.pulse_time = pulse_time/1000

    @pyqtSlot()
    def run(self):
        self.signals.inlet_open.emit()
        self.signals.bypass_close.emit()
        sleep(self.pulse_time)
        self.signals.inlet_close.emit()
        self.signals.bypass_open.emit()
        print('Pulser done')


class TriggerSignals(QObject):
    finished = pyqtSignal()



class Trigger(QRunnable):
    

    #Worker class for pwm trigger
    def __init__(self, aq_time):
        super(Trigger, self).__init__()
        self.aq_time = aq_time
        self.signals = TriggerSignals()

    @pyqtSlot()
    def run(self):
        trigger.run(self.aq_time)         
        print('trigger done')

class mywindow(QMainWindow):
    #class that handles the window and slots from the signals
    def __init__(self):
        
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
    
        self.threadpool = QThreadPool()
    
    def update_inlet_state(self):
        self.ui.inlet_status.setText(inlet.status)

    def update_bypass_state(self):
        self.ui.bypass_status.setText(bypass.status)

  

    def set_auto(self):
        self.ui.inlet_open.setEnabled(False)
        self.ui.inlet_close.setEnabled(False)
        self.ui.bypass_open.setEnabled(False)
        self.ui.bypass_close.setEnabled(False)
        w.bypass.open()
        w.inlet.close()
        self.ui.spin_rest.setEnabled(True)
        self.ui.spin_len.setEnabled(True)
        self.ui.spin_cycles.setEnabled(True)
        self.ui.spin_freq.setEnabled(True)
        self.ui.spin_pulse.setEnabled(True)
        self.ui.run_button.setEnabled(True)

    def set_manual(self):
        self.ui.inlet_open.setEnabled(True)
        self.ui.inlet_close.setEnabled(True)
        self.ui.bypass_open.setEnabled(True)
        self.ui.bypass_close.setEnabled(True)
        self.bypass.open()
        self.inlet.close()
        self.ui.spin_rest.setEnabled(False)
        self.ui.spin_len.setEnabled(False)
        self.ui.spin_cycles.setEnabled(False)
        self.ui.spin_freq.setEnabled(False)
        self.ui.spin_pulse.setEnabled(False)
        self.ui.run_button.setEnabled(False)

    def freq_change(self):
        trigger.frequency =  self.ui.spin_freq.value()

            
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    INLETPIN = 17
    BYPASSPIN = 27
    TRIGGERPIN = 22
    inlet = Valve(INLETPIN, 'Inlet valve')
    bypass = Valve(BYPASSPIN, 'Bypass valve')
    trigger = pwmTrigger(TRIGGERPIN)
    app = QApplication([])
    
    w = mywindow()
    w.inlet = QValve(inlet)
    w.bypass = QValve(bypass)
    w.tasker = Tasker()

    w.ui.inlet_status.setText(inlet.status)
    w.ui.bypass_status.setText(bypass.status)
    
    #Set up inlet signals and slots
    w.ui.inlet_open.clicked.connect(w.inlet.open)
    w.ui.inlet_close.clicked.connect(w.inlet.close)

    #Set up bypass signals and slots
    w.ui.bypass_open.clicked.connect(w.bypass.open)
    w.ui.bypass_close.clicked.connect(w.bypass.close)
    w.inlet.action.connect(w.update_inlet_state)
    w.bypass.action.connect(w.update_bypass_state)


    #Set up the radio buttons
    w.ui.auto_button.toggled.connect(w.set_auto)
    w.ui.manual_button.toggled.connect(w.set_manual)
    w.set_manual()
    
    #Connect the spin boxes with the pwmTrigger
    w.ui.spin_freq.valueChanged.connect(w.freq_change)
    w.ui.spin_pulse.valueChanged.connect(w.tasker.update_pulse_time)
    w.ui.spin_len.valueChanged.connect(w.tasker.update_aq_time)
    w.ui.spin_cycles.valueChanged.connect(w.tasker.update_cycles)
    w.ui.spin_rest.valueChanged.connect(w.tasker.update_rest_time)

    #Connect the TAPXPS buttons
    w.ui.run_button.clicked.connect(w.tasker.run)


    w.show()
    sys.exit(app.exec_())

    GPIO.cleanup()


