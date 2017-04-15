#from FSM_example import *
from output import *
import time

def tic():
    print('Tic !')

def tac():
    print('Tac !')

if __name__ == '__main__':
    fsm = Switch()
    fsm.connect('tic', tic)
    fsm.connect('tac', tac)
    
    fsm.start()
    fsm.submitEvent("SWITCH")
    time.sleep(0.5)
    fsm.submitEvent("SWITCH")
    time.sleep(0.5)
    fsm.stop()
