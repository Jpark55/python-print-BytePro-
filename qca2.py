import pyautogui, time
from win32 import win32api
import win32.lib.win32con as win32con
from tkinter import messagebox

#need to make name option

def qcainput(x):
    if x not in ['adv','disc','rand']:
        messagebox.showerror('requires: adv, disc, or rand')
        return
    for i in range(1, 4):
        if str(pyautogui.locateOnScreen('clips/qca_screen2.PNG',grayscale=True, confidence=0.8)) == "None":
            i = i+1
            time.sleep(1)
            print('looking for qca screen')
        else: 
            break
    if str(pyautogui.locateOnScreen('clips/qca_screen2.PNG',grayscale=True, confidence=0.8)) == "None":
        print('QCA screen not found')
    else:
        qca = pyautogui.locateOnScreen('clips/qca_screen2.PNG',grayscale=True, confidence=0.8)
        time.sleep(1)
        #print(qca) 
        #print(qca[0]) 
        #print(qca[1])
        print('found qca screen')
        win32api.SetCursorPos((qca[0]+28,qca[1]+7))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.1) #pauses for .01 sec
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(3)
    if str(pyautogui.locateOnScreen('clips/qca_name_dates.PNG', confidence=0.8)) =="None":
        print('QCA name box not found')
    else:
        qca2 = pyautogui.locateOnScreen('clips/qca_name_dates.PNG', confidence=0.8)
        #print(qca2) 
        #print(qca2[0]) 
        #print(qca2[1])
        print('found qca name box')
        #name
        #440, 249
        #440, 300
        #749, 248
        win32api.SetCursorPos((qca2[0]+230,qca2[1]+35))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01) #pauses for .01 sec
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        pyautogui.write(['j','j','tab'])
        
        if x == 'adv':
        # Adverse
            win32api.SetCursorPos((qca2[0]+278,qca2[1]+60))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            return
            #time.sleep(1)
        elif x == 'rand':
        # random
            win32api.SetCursorPos((qca2[0]+278,qca2[1]+112))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            return
            #time.sleep(1)
        elif x == 'disc':
        # discretionary
            win32api.SetCursorPos((qca2[0]+587,qca2[1]+60))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            return


#qcainput('rand')