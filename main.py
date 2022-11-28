import tkinter as tk
import os
from tkinter import *
import tkinter.font as font

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
        output = os.system(f"nmap -T5 -sVC {entry} -oN nmap | grep 'scan report\|/tcp' > sort.txt")
        with open('sort.txt') as f:
            portScan = f.read()
        label.config(text=f'{portScan}')

def dyeIp(entry):
    print("[.] Blocking -> ", entry)
    oyo = os.system("echo 'Blocking -> ' > iniEE")
    with open('nmap.txt') as f:
        iniE = f.read()
    label.config(text=f'{iniE}')
    # ayo = os.system(f"iptables -A INPUT -s 192.168.5.137 -j DROP")
    ayo = os.system("echo 'h00di3' | sudo -S ufw deny from 192.168.5.137; echo 'h00di3' | sudo -S ufw default deny outgoing")
    yoo = os.system("echo 'Saved!' > ipTablesSave")
    with open('ipTablesSave') as f:
        endE = f.read()
    label.config(text=f'{endE}')
    print("[.] Saved!")
    

        
def playAni():
    anim = os.system("echo 'h00di3' | sudo -S ufw default allow outgoing;echo 'Vamos!' | cowsay > anim")
    with open('anim') as f:
        cont = f.read()
    label.config(text=f'{cont}')

root = tk.Tk()
root.title("Internal Firewall Management System")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, background='#ff4dff')
canvas.pack()

background_image = tk.PhotoImage(file='black.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bd=5, bg='#92004e')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg='#fdfde8')
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Scan", bg='#262626', fg='#f2f2f2', font=15, command=lambda: scan(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#92004e', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg='#e8f8fd')
label.place(relwidth=1, relheight=1)

on_button = tk.Button(label, text="vamos", bg='#262626', fg='#f2f2f2', font=("Terminal",15), command=playAni)
on_button.place(relx=0.8,rely=0.89, relwidth=0.2, relheight=0.1)

nextBtn = tk.Button(label, text="Services", bg='#252525', fg='#f2f2f2', font=("Helvetica", 10), command=lambda: nextOut(entry.get()))
nextBtn.place(relx=0.9, rely=0.01, relwidth=0.1, relheight=0.1)

ipTab = tk.Button(root, text="Block", bg='#252525', fg='#f2f2f2', font=("Terminal, 15"), command=lambda: dyeIp('nmap.txt'))
ipTab.place(relx=0.65, relheight=0.08, relwidth=0.22)

root.mainloop()