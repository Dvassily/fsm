from StateMachine import *
from enum import Enum
from queue import Queue
import threading, time

class State(Enum):
    OFF = 0
    ON = 1

class Event(Enum):
    SWITCH = 0

class Switch(StateMachine):
    def __init__(self):
        StateMachine.__init__(self, State, Event)
        self.currentState = State.OFF

    def microstep(self, event):
        if (self.currentState == State.OFF):
            if (event == Event.SWITCH):
                self.execute('tic')
                self.currentState = State.ON
        
        elif (self.currentState == State.ON):
            if (event == Event.SWITCH):
                self.execute('tac')
                self.currentState = State.OFF
        
