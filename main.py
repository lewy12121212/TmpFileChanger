#!/usr/bin/env python3.8
import tkinter as tk
from functools import partial
import os
from threading import Thread

default_link = "/etc/xdg/lxsession/LXDE/autostart"

commands = [
  "xset s off",
  "xset s noblank",
  "xset -dpms"
]

window = tk.Tk()
window.geometry("800x500")
window.config(bg="#5e5e5e")
window.resizable(width=False,height=False)
window.title('File changer')

def save_to_autostart():
  print("save...\n")
  print("pam: ", entry_parameter.get(), " link: ", entry_link.get(), "\n")
  
  link_to_file = entry_link.get()
  config_file = open(link_to_file, "a")

  for com in commands:
    config_file.write('\n' + com)

  param = entry_parameter.get()
  browser_link = 'http://misim.pl/monitory-fizyczne/pokaz/' + param
  browser_command = 'chromium-browser --disable-infobars --kiosk ' + browser_link
  config_file.write('\n' + browser_command)
  config_file.close()

def test_connect():
  print("connection test...\n")
  param = entry_parameter.get()
  test_link = "http://misim.pl/monitory-fizyczne/pokaz/" + param
  print("link: ", test_link, "\n")
  os.system('chromium ' + test_link)

label_app_name = tk.Label(window,text="File changer",font=("Arial",20), fg="#dddddd", bg="#212121", height= 1, width=30)

label_link = tk.Label(window,text="Ścieżka: ",font=("Arial",15), fg="White", bg='#5e5e5e')
entry_link = tk.Entry(window,font=("Arial",18), width=30, textvariable=tk.StringVar())
entry_link.insert(tk.END, default_link)

label_parameter = tk.Label(window,text="Parametr:",font=("Arial",15), fg="White", bg='#5e5e5e')
entry_parameter = tk.Entry(window,font=("Arial",18), width=30, textvariable=tk.StringVar())

button_save = tk.Button(window,text="ZAPISZ W AUTOSTART",font=("Arial",15), fg="#dddddd", height= 1, width=30, command=save_to_autostart)
button_test = tk.Button(window,text="TEST",font=("Arial",15), fg="#dddddd", height= 1, width=30, command=test_connect)
button_exit = tk.Button(window,text="WYJŚCIE",font=("Arial",15), fg="#dddddd", height= 1, width=30, command=exit)

label_app_name.place(x=50,y=20)

label_link.place(x=50,y=100)
entry_link.place(x=200,y=100)

label_parameter.place(x=50,y=160)
entry_parameter.place(x=200,y=160)

button_save.place(x=50,y=220)
button_test.place(x=50, y=280)
button_exit.place(x=50, y=340)

window.mainloop()