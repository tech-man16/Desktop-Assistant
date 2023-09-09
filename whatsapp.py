import pyautogui,time

start = time.time()
screenwidth , screenheight = pyautogui.size()
print(f"{screenwidth} x {screenheight}")

#pyautogui.hotkey('win','6')   # opens Whatsapp

def sendBdMsg(name):
    pyautogui.moveTo(240,1058,duration=1)
    pyautogui.click()

    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    pyautogui.write("whatsapp",0.5)
    pyautogui.moveTo(255,411,duration=1)
    pyautogui.click()

    pyautogui.moveTo(180,151,duration=1)  # At Search bar
    #time.sleep(2)
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.write(name,0.25)  # write to the recipient name
    pyautogui.moveTo(250,240,duration=1)  # At target Recepient
    #time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(1007,1001,duration=1) # At message point
    pyautogui.hotkey('ctrl','a') # Delete any draft message if any !!

    pyautogui.write(f"Happy Birthday !!! {name}",0.25)
    pyautogui.moveTo(1890,1001,duration=1)
    pyautogui.click()

#sendWpMsg("Satya")

#end = time.time()
#print((end-start) * 10**3,"ms")