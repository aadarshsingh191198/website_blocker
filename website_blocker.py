# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 01:22:49 2018

@author: AADARSH
"""


from tkinter import *
import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
website_list =    ["www.facebook.com","www.google.com"]
redirect = "127.0.0.1"

def start():
    
    with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        file.write(redirect + " " + website + "\n")
    B2['state']='normal'
    B1['state']='disabled'
                        
def stop():
    
    with open(hosts_path, 'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
     
        # removing hostnmes from host file
        file.truncate()
    B1['state']='normal'
    B2['state']='disabled'

def add(webs):
    #print(strvar, website)
    #print("Hello")
    if webs!="":
        website_list.append(webs)
        website.set("")
        listbox.insert(END, webs)

def deleter():
    index = listbox.curselection()[0]
    listbox.delete(ANCHOR)
    website_list.pop(index)
    print(website_list)
    
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Blocker")
    gui.geometry("265x400")

    B1 = Button(gui, text ="Start", command = start)
    B1.pack()
    B2 = Button(gui, text ="Stop", command = stop)
    B2.pack() 
    B2['state']='disabled'
    website = StringVar()
    E1 = Entry(gui,textvariable=website)
    E1.pack()
    B3 = Button(gui, text ="Add", command = lambda:add(website.get()))
    B3.pack() 
    var = StringVar()
    label = Label( gui, textvariable=var )
    var.set("Blocked Websites")
    label.pack()
    listbox = Listbox(gui)
    listbox.pack()

    for item in website_list:
        listbox.insert(END, item)

    B4 = Button(gui, text="Delete", command=deleter)
    B4.pack()
    
    # start the GUI
    gui.mainloop()