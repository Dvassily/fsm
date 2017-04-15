from enum import Enum
from queue import Queue
import threading
import time

class StateMachine:
    def __init__(self, states, events):
        self.currentState = None
        self.isRunning = False
        self.internalQueue = Queue()
        self.externalQueue = Queue()
        self.actions = {}
        self.states = states;
        self.events = events;
        
    def mainLoop(self):
        while self.isRunning:
            while not self.externalQueue.empty():
                event = self.externalQueue.get()
                self.microstep(event)

    def submitEvent(self, eventStr):
        try:
            self.externalQueue.put(self.events[eventStr])
        except KeyError:
            print('Error : Unknown event ' + eventStr)

    def connect(self, actionStr, handler):
        self.actions[actionStr] = handler;
    
    def start(self):
        self.isRunning = True
        threading.Thread(target=self.mainLoop).start()

    def execute(self, actionStr):
        try:
            self.actions[actionStr]()
        except KeyError:
            print('Action ' + actionStr + ' not handled')

    def stop(self):
        self.isRunning = False
