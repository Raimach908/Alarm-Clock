from tkinter import *  
import datetime as dt
import time
from pygame import mixer
from tkinter import messagebox

mixer.init()

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = dt.datetime.now()
        current_time_str = current_time.strftime("%H:%M:%S")
        print("\t\t Current Time:", current_time_str)
        if current_time_str == set_alarm_timer:
            mixer.music.load('D:/python/Alarm Clock/music.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('Info','Alarm Time Reached! Wake Up!')
            if msg == 'ok':
                mixer.music.stop()    
            break

def getAlarmTime():
    global alarm_set
    alarm_set = False
    setAlarm = f"{Hour.get()}:{Minute.get()}:{second.get()}"
    print("\n\t\t Set Alarm Time: ",setAlarm,"\n")
    alarm(setAlarm)

# Creating GUI Window
guiWindow = Tk()  
guiWindow.title("The alarm clock")
guiWindow.geometry("430x250+350+150")  # (width*height*x_coordinate*y_coordinate)
guiWindow.iconbitmap('d:/python/Alarm Clock/icon.ico')
guiWindow.resizable(width=False, height=False)  
guiWindow.config(bg="#636262")

image = PhotoImage(file='D:/python/Alarm Clock/bg.png')
bg_label = Label(guiWindow, image=image)
bg_label.place(relwidth=1, relheight=1)

timeFormat = Label(guiWindow, text="Remember to set time in 24-hour format!", fg="white", bg="#313131", font = ("Times new roman",13))
timeFormat.place(x=2, y=210)
add_time = Label(guiWindow, text=" Hour      Minute     Second",font = ("Times new roman",16), fg="white", bg="#313131")
add_time.place(x=35, y=55)

Hour = StringVar()
Minute = StringVar()
second = StringVar()

hourTime = Entry(guiWindow, textvariable=Hour, background="#FFFFE0", font=20, width=4)
hourTime.grid(row=4, column=0,padx = 40,pady=94)
minuteTime = Entry(guiWindow, textvariable=Minute, font=20, width=4, background="#FFFFE0")
minuteTime.grid(row=4, column=1,padx = 0,pady=90)
secondTime = Entry(guiWindow, textvariable=second, font=20, width=4, background="#FFFFE0")
secondTime.grid(row=4, column=2,padx = 37,pady=94)

submit = Button(guiWindow, text="Set the time", foreground="white", background="#4D8152", width=12,font = ("Times new roman",15,"bold"), command=getAlarmTime)
submit.place(x=80, y=130)

guiWindow.mainloop()

print("\n\t\t Alarm has been closed!")
