from StateMachine import *
from enum import Enum
from queue import Queue
import threading, time

class State(Enum):
    State_1 = 0
    State_2 = 1

class Event(Enum):
    in1 = 0
    in2 = 1

class RaiseTest(StateMachine):
    def __init__(self):
        super(RaiseTest, self).__init__(State, Event)
        self.currentState = State.State_1

    def microstep(self, event):
        if (self.currentState == State.State_1):
            if (event == Event.in1):
                self.internalQueue.put(Event['in2'])
                self.enterState(State.State_2)
        
        elif (self.currentState == State.State_2):
            if (event == Event.in2):
                self.execute('action2')
                self.enterState(State.State_1)

        
