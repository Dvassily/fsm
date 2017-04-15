#from FSM_example import *
#from output import *
#from rsoutput import *
from slideoutput import *
import time

# def tic():
#     print('Tic !')

# def tac():
#     print('Tac !')

# def action2():
#     print('! action2 !')
    
# if __name__ == '__main__':
#     fsm = Switch()
#     fsm.connect('tic', tic)
#     fsm.connect('tac', tac)
    
#     fsm.start()
#     fsm.submitEvent("SWITCH")
#     time.sleep(0.5)
#     fsm.submitEvent("SWITCH")
#     time.sleep(0.5)
#     fsm.stop()

# if __name__ == '__main__':
#     fsm = RaiseTest()
#     fsm.connect('action2', action2)
    
#     fsm.start()
#     fsm.submitEvent("in1")
#     time.sleep(0.5)
#     fsm.stop()

def startClosingMotor():
    print('Start closing motor')
    
def stopClosingMotor():
    print('Stop closing motor')
    
def startOpeningMotor():
    print('Start opening motor')
    
def stopOpeningMotor():
    print('Stop opening motor')    

if __name__ == '__main__':
    fsm = Slide()
    fsm.connect('startClosingMotor', startClosingMotor)
    fsm.connect('stopClosingMotor', stopClosingMotor)
    fsm.connect('startOpeningMotor', startOpeningMotor)
    fsm.connect('stopOpeningMotor', stopOpeningMotor)
    
    fsm.start()
    fsm.submitEvent("close")
    time.sleep(0.5)
    fsm.submitEvent("isClosed")
    time.sleep(0.5)
    fsm.submitEvent("open")
    time.sleep(0.5)
    fsm.submitEvent("isOpened")
    time.sleep(0.5)
    fsm.submitEvent("stop")
    #fsm.stop()
