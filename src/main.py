from sys import stdin
from enum import Enum
from lxml import etree

class FSMGenerator:
    def __init__(self, inputFilePath, outputFilePath, name):
        self.root = etree.parse(inputFilePath)
        self.outputFilePath = outputFilePath
        self.name = name

    def append_to_file(self, content, indentLevel = 0):
        for i in range(indentLevel * 4):
            self.outputFile.write(' ')
        self.outputFile.write(content)        
        
    def generate_import(self):
        self.append_to_file('from StateMachine import *\n')
        self.append_to_file('from enum import Enum\n')
        self.append_to_file('from queue import Queue\n')
        self.append_to_file('import threading, time\n\n')

    def generate_states(self):
        states = self.root.xpath("//scxml/final|state")

        self.append_to_file('class State(Enum):\n')

        i = 0
        for node in states:
            self.append_to_file(node.get('id') + ' = ' + str(i) + '\n', 1)
            i += 1

        self.append_to_file('\n')

    def generate_events(self):
        events = self.root.xpath('//scxml/state/transition')
        processed = []
        
        self.append_to_file('class Event(Enum):\n')

        i = 0
        for node in events:
            event = node.get('event')

            if event not in processed:
                self.append_to_file(event + ' = ' + str(i) + '\n', 1)
                processed.append(event)
                i += 1

        self.append_to_file('\n')

    def generate_transition(self, transitions):
        nbTransition = 0
        for transition in transitions:
            transitionCondition = ('el' if (nbTransition > 0) else '') + 'if (event == Event.' + transition.get('event') + '):\n'
            self.append_to_file(transitionCondition, 3)
            for sendNode in transition.findall('send'):
                self.append_to_file('self.execute(\'' + sendNode.get('event') + '\')\n', 4)
            for raiseNode in transition.findall('raise'):
                self.append_to_file('self.internalQueue.put(Event[\'' + raiseNode.get('event') + '\'])\n', 4)                

            self.append_to_file('self.enterState(State.' + transition.get('target') + ')\n', 4)
        

    def generate_microstep(self):
        states = self.root.xpath('//scxml/state')
        self.append_to_file('def microstep(self, event):\n', 1)

        nbState = 0
        for node in states:
            stateCondition = ('el' if (nbState > 0) else '') + 'if (self.currentState == State.' + node.get('id') + '):\n'
            self.append_to_file(stateCondition, 2)
            self.generate_transition(node.findall('transition'))
            self.append_to_file('\n', 2);
            nbState += 1
        
    def generate_class(self):
        initial = self.root.xpath('//scxml/state')[0].get('id')
        
        self.append_to_file('class ' + self.name + '(StateMachine):\n')
        self.append_to_file('def __init__(self):\n', 1)
        self.append_to_file('super(' + self.name + ', self).__init__(State, Event)\n', 2)
        self.append_to_file('self.currentState = State.' + initial + '\n', 2)
        self.append_to_file('self.finalStates = [ ', 2)

        finalNodes = self.root.xpath('//scxml/final')
        self.append_to_file('State.' + finalNodes[0].get('id'))
        for final in finalNodes[1:]:
            self.append_to_file(', State.' + final.get('id'))
        self.append_to_file(' ]\n\n')
        
        self.generate_microstep()
        
    def generate(self):
        self.outputFile = open(self.outputFilePath, 'w')
        
        self.generate_import()
        self.generate_states()
        self.generate_events()
        self.generate_class()
        
        self.outputFile.close()
        
if __name__ == '__main__':
    #gen = FSMGenerator('../switch.xml', 'output.py', 'Switch')
    #gen = FSMGenerator('../raisetest.scxml', 'rsoutput.py', 'RaiseTest')
    gen = FSMGenerator('../slide.scxml', 'slideoutput.py', 'Slide')
    gen.generate()
