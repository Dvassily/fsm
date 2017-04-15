from chronooutput import *
from tkinter import *
import time
#fsm.submitEvent("close")

fsm = Chrono()

fsm.start()

def startStop():
    fsm.submitEvent('startStop')
    
def pause():
    print('')    

    window=Tk()
    window.title('StopWatch')

message = Label(window,font=('sans', 20, 'bold'),text="Chrono prêt")
message.grid(row=1)
startBtn = Button(window,text='Start',command=startStop).grid(row=2)
stopBtn  = Button(window,text='Pause',command=pause).grid(row=3)
#pauseBtn = Button(window,text='Pause',command=reset_chrono).grid(row=4)
#Button(window,text='PAUSE !',command=lancer_chrono).grid(row=2)

#fsm.connect('startClosingMotor', startClosingMotor)
window.mainloop()
fsm.stop()

