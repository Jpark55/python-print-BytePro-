import pyautogui, time
from win32 import win32api
import win32.lib.win32con as win32con
from tkinter import messagebox

def printappr(a):
    if a not in ['Corr','WS']:
        messagebox.showerror('requires: Corr or WS')
        return

    if a == 'Corr':
        if str(pyautogui.locateOnScreen('clips/print_button.PNG')) == "None":
            print('Print button not found')
        else:
            b = pyautogui.locateOnScreen('clips/print_button.PNG')
            # print(b) print(b[0]) print(b[1])
            win32api.SetCursorPos((b[0]+43,b[1]+18))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(2.0) # wait for lag of print screen to pop up
            for i in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/print_set_dropdown.png')) == "None":
                    i = i+1
                    time.sleep(1)
                    print('looking for print set dropdown')
                elif str(pyautogui.locateOnScreen('clips/print_set_dropdown.png')) != "None":
                    c = pyautogui.locateOnScreen('clips/print_set_dropdown.png')
                    win32api.SetCursorPos((c[0]+30,c[1]+30))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    win32api.SetCursorPos((c[0]+60,c[1]+60))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)       
                else:
                    print('unable to locate print set dropdown')     
                    break
            for i in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/corr_deselect.png')) == "None":
                    i = i+1
                    time.sleep(1)
                    print('looking for appr de-select')
                elif str(pyautogui.locateOnScreen('clips/corr_deselect.png')) != "None":
                    c = pyautogui.locateOnScreen('clips/corr_deselect.png')
                    win32api.SetCursorPos((c[0]+10,c[1]+10))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:
                    print('unable to locate appr de-select')
                    break
            for i in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/print_confirm_button.png')) == "None":
                    i = i+1
                    time.sleep(1)
                    print('looking for print button')
                elif str(pyautogui.locateOnScreen('clips/print_confirm_button.png')) != "None":
                    c = pyautogui.locateOnScreen('clips/print_confirm_button.png')
                    # print(c) print(c[0]) print(c[1])
                    win32api.SetCursorPos((c[0]+30,c[1]+30))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:   
                    print('unable to locate print button')
                    break
            for x in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/print_confirm2_button.png')) == "None":
                    x = x+1
                    time.sleep(1)
                    print('looking for print confirmation')
                elif str(pyautogui.locateOnScreen('clips/print_confirm2_button.png')) != "None":
                    #time.sleep(2)  # wait for lag of print screen
                    d = pyautogui.locateOnScreen('clips/print_confirm2_button.png')
                    time.sleep(1)
                    #print(d) 
                    #print(d[0]) 
                    #print(d[1])
                    win32api.SetCursorPos((d[0]+40,d[1]+20))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:   
                    print('unable to locate print confirmation')
                    break
            for y in range(1, 5):
                if str(pyautogui.locateOnScreen('clips/print_doc_type_list.png')) == "None":
                    y = y+1
                    time.sleep(1)
                    print('looking for doc type list')
                elif str(pyautogui.locateOnScreen('clips/print_doc_type_list.png')) != "None":
                    #time.sleep(7)  #--wait for lag of document selection screen
                    d = pyautogui.locateOnScreen('clips/print_doc_type_list.png')
                    # print(d) print(d[0]) print(d[1])
                    win32api.SetCursorPos((d[0]+70,d[1]+23))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    pyautogui.write(['u','down','tab','tab','tab','a','tab','tab','tab','tab','tab','enter'])
                else:   
                    print('unable to locate doc type list')
                    break
    elif a == 'WS':
        if str(pyautogui.locateOnScreen('clips/print_button.PNG')) == "None":
            print('Print button not found')
        else:
            b = pyautogui.locateOnScreen('clips/print_button.PNG')
            # print(b) print(b[0]) print(b[1])
            win32api.SetCursorPos((b[0]+43,b[1]+18))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(2.0) # wait for lag of print screen to pop up
            win32api.SetCursorPos((1040,651))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(1.0)
            win32api.SetCursorPos((1040,684))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01) #pauses for .01 sec
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

            for i in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/print_confirm_button.png')) == "None":
                    i = i+1
                    time.sleep(1)
                    print('looking for print button')
                elif str(pyautogui.locateOnScreen('clips/print_confirm_button.png')) != "None":
                    c = pyautogui.locateOnScreen('clips/print_confirm_button.png')
                    # print(c) print(c[0]) print(c[1])
                    win32api.SetCursorPos((c[0]+30,c[1]+30))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:   
                    print('unable to locate print button')
                    break

            for x in range(1, 4):
                if str(pyautogui.locateOnScreen('clips/print_confirm2_button.png')) == "None":
                    x = x+1
                    time.sleep(1)
                    print('looking for print confirmation')
                elif str(pyautogui.locateOnScreen('clips/print_confirm2_button.png')) != "None":
                    #time.sleep(2)  # wait for lag of print screen
                    d = pyautogui.locateOnScreen('clips/print_confirm2_button.png')
                    time.sleep(1)
                    #print(d) 
                    #print(d[0]) 
                    #print(d[1])
                    win32api.SetCursorPos((d[0]+40,d[1]+20))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:   
                    print('unable to locate print confirmation')
                    break

            for y in range(1, 5):
                if str(pyautogui.locateOnScreen('clips/print_doc_type_list.png')) == "None":
                    y = y+1
                    time.sleep(1)
                    print('looking for doc type list')
                elif str(pyautogui.locateOnScreen('clips/print_doc_type_list.png')) != "None":
                    #time.sleep(7)  #--wait for lag of document selection screen
                    d = pyautogui.locateOnScreen('clips/print_doc_type_list.png')
                    # print(d) print(d[0]) print(d[1])
                    win32api.SetCursorPos((d[0]+70,d[1]+23))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    time.sleep(0.01) #pauses for .01 sec
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                    pyautogui.write(['u','down','tab','tab','tab','a','tab','tab','tab','tab','tab','enter'])
                else:
                    print('unable to locate doc type list')   
                    break
        


