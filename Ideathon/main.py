from tkinter import *
from tkinter import Button
import tkinter as tk
import os
import signal

def scan(entry):
        print("[+] pinging!", entry)
        response = os.system(f"nmap -n -sP {entry}"+" | grep report | awk {'print $5'} > ping.txt")
        with open('ping.txt') as f:
            hosts = f.read()
            label.config(text=f'These Hosts Are Up:\n {hosts}', fg="#A8E6CE", font=("SimSun", 17))
            

def scan_ip_range(entry):
    print("[+] Port Scanning : ", entry)
    output = os.system(f"echo 'password' | sudo -S nmap -T5 -sS {entry} -oN nmap_output.txt | grep 'scan report\|/tcp\|MAC' > sort.txt")
    with open('sort.txt') as f:
        portScan = f.read()
        label.config(text=f'{portScan}', fg="#A8E6CE", font=("Helvetica", 17))

def block_ip(ip_entry):
    # Get the IP address from the entry field
    # os.system("iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT")

    print("[+] Blocking Ip : ", ip_entry)
    os.system(f"echo 'password' | sudo -S iptables -A INPUT -s {ip_entry} -j DROP")
    blocking = os.system("echo 'Blocked Successfully !' | cowsay > block.txt")
    with open('block.txt') as f:
         block = f.read()
         label.config(text=f'{block}', fg="#FE7A15", font=("Consolas", 20))


def allow_ip():
    print("[+] Allowing Ip... DONE!")
    os.system("echo 'password' | sudo -S iptables -F")
    blocking = os.system("echo 'Accepted Sucessfully !' | cowsay > accept.txt")
    with open('accept.txt') as f:
        accept = f.read()
        label.config(text=f'{accept}', fg="#D3DD18", font=("Consolas", 20))

def displayRules():
    os.system("echo 'List Of Logs: \n' > ipRules.txt")
    ipRules = os.system("echo 'password' | sudo -S iptables -L | grep 'anywhere' | head -n 10 >> ipRules.txt")
    with open('ipRules.txt') as f:
        blocked_ips = f.read()
        label.config(text=f'{blocked_ips}', fg="#C2649A", font=("Helvetica", 17))

def playAni():
    os.system("echo 'password' | sudo -S systemctl start apache2; echo 'password' | sudo -S iptables -I INPUT -p tcp -m tcp --dport 7777 -j ACCEPT")
    animation = os.system('echo "Server is up and running..." > vamos.txt; echo "Vamos !" | cowsay >> vamos.txt')
    with open('vamos.txt') as f:
        cow = f.read()
        label.config(text=f'{cow}', fg="#ffcad4", font=("Consolas", 20))

def exitFunction():
    exiting = os.system("echo 'password' | sudo -S systemctl stop apache2; echo 'password' | sudo -S iptables -A INPUT -p tcp -m tcp --dport 7777 -j DROP")
    messsage = os.system("echo 'SERVER DOWN' | figlet -f block > message.txt")
    with open('message.txt') as f:
        msg = f.read()
        label.config(text=f'{msg}', fg="#ff005f", font=20)

root = tk.Tk()
root.title("Internal Firewall Management System")
icon = tk.PhotoImage(file="exploitcat.png")
root.iconphoto(False, icon)
root.configure(bg="#0b0742")

frame = tk.Frame(root, bd=5, bg='#e5eaf5')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40, bg='#FBEEE6')
entry.place(relwidth=0.65, relheight=1)

ip_entry = tk.Entry(root, font=40, bg='#FFE5D8')
ip_entry.place(relx=0.39,rely=0.003, relheight=0.08, relwidth=0.22)

scan_button = tk.Button(frame, text="Scan", bg='#494D5F', fg='#a0d2eb', font=("SimSun", 17), command=lambda: scan(entry.get()))
scan_button.place(relx=0.7, relwidth=0.15, relheight=1)

lower_frame = tk.Frame(root, bg='#e5eaf5', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.75, anchor='n')

label = tk.Label(lower_frame, bg='#2A363B')
label.place(relwidth=1, relheight=1)

on_button = tk.Button(root, text="Vamos", bg='#494D5F', fg='#a0d2eb', font=("Consolas",15), command=playAni)
on_button.place(relx=0.895,rely=0.12, relwidth=0.09, relheight=0.067)
on_button.configure(highlightthickness=0)

nextBtn = tk.Button(frame, text="Ports", bg='#494D5F', fg='#a0d2eb', font=("Consolas", 17), command=lambda: scan_ip_range(entry.get()))
nextBtn.place(relx=0.85, relwidth=0.15, relheight=1)

ipDye = tk.Button(root, text="Block", bg='#494D5F', fg='#a0d2eb', font=("Consolas", 10), command=lambda: block_ip(ip_entry.get()))
ipDye.place(relx=0.62,rely=0.014, relheight=0.05, relwidth=0.07)

ipAlive = tk.Button(root, text="Allow", bg='#494D5F', fg='#a0d2eb', font=("Consolas", 10), command=allow_ip)
ipAlive.place(relx=0.31,rely=0.014, relheight=0.05, relwidth=0.07)

list_btn = tk.Button(root, text="List", bg='#494D5F', fg='#a0d2eb', font=("Consolas", 12), command=displayRules)
list_btn.place(relx=0.895, rely=0.037, relwidth=0.09, relheight=0.067)
list_btn.configure(highlightthickness=2)

exit_btn = tk.Button(root, text="Exit", bg='#494D5F', fg='#a0d2eb', font=("Consolas", 15), command=exitFunction)
exit_btn.place(relx=0.895, rely=0.19, relwidth=0.09, relheight=0.067)
exit_btn.configure(highlightthickness=0)

root.mainloop()
