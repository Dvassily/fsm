from StateMachine import *
from enum import Enum
from queue import Queue
import threading, time

class State(Enum):
    INIT = 0
    RUNNING = 1
    PAUSED = 2
    STOPPED = 3

class Event(Enum):
    startStop = 0
    pauseResume = 1

class Chrono(StateMachine):
    def __init__(self):
        super(Chrono, self).__init__(State, Event)
        self.enterState(State.INIT)
    
    def microstep(self, event):
        if (self.currentState == State.INIT):
            if (event == Event.startStop):
                self.execute('start')
                self.enterState(State.RUNNING)
        
        elif (self.currentState == State.RUNNING):
            if (event == Event.pauseResume):
                self.execute('pause')
                self.enterState(State.PAUSED)
            if (event == Event.startStop):
                self.execute('stop')
                self.enterState(State.STOPPED)
        
        elif (self.currentState == State.PAUSED):
            if (event == Event.pauseResume):
                self.execute('resume')
                self.enterState(State.RUNNING)
            if (event == Event.startStop):
                self.enterState(State.STOPPED)
        
        elif (self.currentState == State.STOPPED):
            if (event == Event.startStop):
                self.execute('reset')
                self.enterState(State.INIT)
        
