from StateMachine import *
from enum import Enum
from queue import Queue
import threading, time

class State(Enum):
    opened = 0
    isClosing = 1
    closed = 2
    isOpening = 3
    final = 4

class Event(Enum):
    close = 0
    stop = 1
    isClosed = 2
    open = 3
    isOpened = 4

class Slide(StateMachine):
    def __init__(self):
        super(Slide, self).__init__(State, Event)
        self.currentState = State.opened
        self.finalStates = [ State.final ]

    def microstep(self, event):
        if (self.currentState == State.opened):
            if (event == Event.close):
                self.execute('startClosingMotor')
                self.enterState(State.isClosing)
            if (event == Event.stop):
                self.enterState(State.final)
        
        elif (self.currentState == State.isClosing):
            if (event == Event.isClosed):
                self.execute('stopClosingMotor')
                self.enterState(State.closed)
        
        elif (self.currentState == State.closed):
            if (event == Event.open):
                self.execute('startOpeningMotor')
                self.enterState(State.isOpening)
            if (event == Event.stop):
                self.enterState(State.final)
        
        elif (self.currentState == State.isOpening):
            if (event == Event.isOpened):
                self.execute('stopOpeningMotor')
                self.enterState(State.opened)
        
