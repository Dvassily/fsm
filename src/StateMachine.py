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
        self.eventThread = threading.Thread(target=self.mainLoop)
        self.finalStates = []
        
    def mainLoop(self):
        while self.isRunning:
            while not self.internalQueue.empty():
                self.handleEvent(self.internalQueue.get())
            
            event = self.externalQueue.get()
            if event is not None:
                self.handleEvent(event)

    def handleEvent(self, event):
        print('Fire transition ' + event.name)
        self.microstep(event)
        
        if self.currentState in self.finalStates:
            self.stop()

    def enterState(self, state):
        self.currentState = state
        print('Enter state ' + state.name)

    def submitEvent(self, eventStr):
        try:
            self.externalQueue.put(self.events[eventStr])
        except KeyError:
            print('Error : Unknown event ' + eventStr)

    def connect(self, actionStr, handler):
        self.actions[actionStr] = handler;

    def start(self):
        self.isRunning = True
        self.eventThread.start()

    def execute(self, actionStr):
        try:
            self.actions[actionStr]()
        except KeyError:
            print('Action ' + actionStr + ' not handled')

    def stop(self):
        self.isRunning = False
        self.externalQueue.put(None)
