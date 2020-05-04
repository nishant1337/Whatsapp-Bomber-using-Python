import tkinter as tk
from tkinter import *
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os,time
def startexe():
    victimname = str(name.get())
    msg = str(msgg.get())
    num = nooo.get()
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    #15 second for scan
    time.sleep(15)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(victimname))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    for i in range(num):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)

        # button = driver.find_element_by_class_name('_3M-N-')
        # button.click()
#GUI
win=tk.Tk()
win.title("Whatsapp bomber by NISHANT")
win.geometry("600x600")
x=Label(win,text="YOU HAVE 15 SECONDS TO SCAN AND LOGIN").place(x=140,y=10)
x=Label(win,text="Enter name").place(x=150,y=100)
name=StringVar()
namebox=Entry(win,textvariable=name).place(x=250,y=100)

x=Label(win,text="Enter massage").place(x=150,y=200)

msgg=StringVar()
nmsgbox=Entry(win,textvariable=msgg).place(x=250,y=200)

x=Label(win,text="No of msg").place(x=150,y=300)
nooo=IntVar()
nobox=Entry(win,textvariable=nooo).place(x=250,y=300)

tk.Button(win,text="START BOMBING",command=startexe).place(x=250,y=390)

win.mainloop()
