import threading
from chronooutput import *
from tkinter import *
import time
import datetime


class ChronoTest:
    def __init__(self):
        self.running = False
        self.updateTime()
        self.window=Tk()
        self.window.title('StopWatch')
        self.display = Label(self.window,font=('sans', 20, 'bold'),text="Chrono prêt")
        self.display.grid(row=1)
        self.startBtn = Button(self.window,text='Start',command=self.startStop)
        self.startBtn.grid(row=2)
        self.pauseBtn  = Button(self.window,text='Pause',command=self.pauseResume)
        self.pauseBtn.grid(row=3)
        self.timer = None
        self.beginTime = None
        self.fsm = Chrono()
        self.fsm.connect('stop', self.stop)
        self.fsm.connect('start', self.start)
        self.fsm.connect('reset', self.reset)
        self.fsm.connect('pause', self.pause)
        self.fsm.connect('resume', self.resume)
        self.fsm.start()
        self.window.mainloop()

    def startStop(self):
        self.fsm.submitEvent('startStop')
            
    def pauseResume(self):
        self.fsm.submitEvent('pauseResume')

    def start(self):
        self.startBtn.config(text='Stop')
        self.beginTime = datetime.datetime.now()
        self.running = True
        
    def stop(self):
        self.startBtn.config(text='Reset')
        self.running = False

    def reset(self):
        self.startBtn.config(text='Start')
        self.display.config(text=str(0.0))

    def pause(self):
        self.pauseBtn.config(text='Resume')
        self.running = False;
        
    def resume(self):
        self.pauseBtn.config(text='Pause')
        self.running = True;

    def updateTime(self):
        if self.running:
            self.display.config(text=str((datetime.datetime.now() - self.beginTime).total_seconds()))
        self.timer = threading.Timer(0.1, self.updateTime)
        self.timer.start()
        
stopWatch = ChronoTest()
