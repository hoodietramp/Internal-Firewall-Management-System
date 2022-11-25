import tkinter as tk
import os
from tkinter import *

HEIGHT = 600
WIDTH = 800

def scan(entry):
        print("[+] pinging!", entry)
        response = os.system(f"nmap -n -sP {entry}"+" | grep report | awk {'print $5'} > nmap.txt")
        with open('nmap.txt') as f:
            contents = f.read()
            label.config(text=f'These Hosts Are Up:\n {contents}')

def nextOut(entry):
        print("[+] Port Scanning : ", entry)
        output = os.system(f"nmap -T5 -sVC -p22,80 {entry} -oN nmap | grep '/tcp' > sort.txt")
        with open('sort.txt') as f:
            portScan = f.read()
        label.config(text=f'{portScan}')

def dyeIp(entry):
    print("[.] Blocking -> ", entry)
    oyo = os.system("echo 'Blocking -> ' > iniEE")
    with open('iniEE') as f:
        iniE = f.read()
    label.config(text=f'{iniE}')    
    ayo = os.system(f"iptables -A OUTPUT -s {entry} -j DROP; service iptables save")
    yoo = os.system("echo 'Blocked Successfully!' > ipTablesSave")
    with open('ipTablesSave') as f:
        endE = f.read()
    label.config(text=f'{endE}')
    print("[.] Blocked Successfully!")
    

        
def playAni():
    anim = os.system("echo 'Vamos!' | cowsay > anim")
    with open('anim') as f:
        cont = f.read()
    label.config(text=f'{cont}')

root = tk.Tk()
root.title("Network Scanner And IP Blocker")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, background='#ff4dff')
canvas.pack()

background_image = tk.PhotoImage(file='black.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bd=5, bg='#fde8ed')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg='#fdfde8')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Scan", bg='#262626', fg='#f2f2f2', font=5, command=lambda: scan(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#fde8ed', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='#e8f8fd')
label.place(relwidth=1, relheight=1)

on_button = tk.Button(label, text="Play", bg='#262626', fg='#f2f2f2', font=("Terminal",21), command=playAni)
on_button.place(relx=0.8,rely=0.89, relwidth=0.2, relheight=0.1)

nextBtn = tk.Button(label, text="Next", bg='#252525', fg='#f2f2f2', font=("Terminal", 15), command=lambda: nextOut(entry.get()))
nextBtn.place(relx=0.9, rely=0.01, relwidth=0.1, relheight=0.1)

ipTab = tk.Button(root, text="Block", bg='#252525', fg='#f2f2f2', font=("Terminal, 15"), command=lambda: dyeIp(entry.get()))
ipTab.place(relx=0.65, relheight=0.08, relwidth=0.22)

root.mainloop()