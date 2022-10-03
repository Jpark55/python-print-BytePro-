from multiprocessing.sharedctypes import Value
from tkinter import *
import qca2
import time
import print_app

#missing auditor name

app = Tk()

switch_frame = Frame(app)
switch_frame.pack()
switch_variable = StringVar(value="WS")
switch = 'WS'

frame = Frame(app)
frame.pack()

bottomframe = Frame(app)
bottomframe.pack( side = BOTTOM )

def set_WS():
    global switch
    switch = 'WS'
    WS_button.config(selectcolor='#00ff00',fg='black')
    Corr_button.config(bg='#8f8f8f',fg='white')
def set_Corr():
    global switch
    switch = 'Corr'
    Corr_button.config(selectcolor='#00ff00',fg='black')
    WS_button.config(bg='#8f8f8f',fg='white')
def advqc():
    qca2.qcainput('adv')
    time.sleep(1)
    print_app.printappr(switch)
def discqc():
    qca2.qcainput('disc')
    time.sleep(1)
    print_app.printappr(switch)
def randqc():
    qca2.qcainput('rand')
    time.sleep(1)
    print_app.printappr(switch)
def printws():
    print_app.printappr(switch)

#WS_Corr Toggle
WS_button   = Radiobutton(switch_frame, text="Wholesale", variable=switch_variable,indicatoron=False, value="WS", width=10, command=set_WS,selectcolor='#00ff00')
Corr_button = Radiobutton(switch_frame, text="Correspondent", variable=switch_variable,indicatoron=False, value="Corr", width=10, command=set_Corr,bg='#8f8f8f',fg='white')
WS_button.pack(side = LEFT)
Corr_button.pack(side = LEFT)
#adverse
adverse_button = Button(frame, text="Adverse", command=advqc)
adverse_button.pack(side = LEFT)
#discretionary
discretionary_button = Button(frame, text="Discretionary", command=discqc)
discretionary_button.pack(side = LEFT)
#random
random_button = Button(frame, text="Random", command=randqc)
random_button.pack(side = LEFT)
#print_ws
random_button = Button(bottomframe, text="Print Approval", command=printws)
random_button.pack(side = LEFT)

app.title('PC QCA')
app.geometry('250x80')

# Start program
app.mainloop()