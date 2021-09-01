import threading 
import socket as s
import os
k=s.socket(s.AF_INET, s.SOCK_DGRAM)
own_ip=input("Enter the your ip or hostname : ")
own_port=1234
other_ip=input("Enter the other ip or hostname ")
other_port=5678
k.bind((own_ip,own_port))
#name=input("enter your name : " )
os.system("clear")
os.system("tput setaf 6")
os.system("banner msg.in")
os.system("tput setaf 7")
#print("-------------------- Chat Program -----------------") 
print()
def send():
  name=input("Your Name:")
  name=name.encode()
  delimiter=" : "
  delimiter=delimiter.encode()
  while True:
    mes=input("to send : ")
    mes=mes.encode()
    #name=name.encode()
    #delimiter=delimiter.encode()
    k.sendto(name+delimiter+mes,(other_ip,other_port))
def recv():
  while True:
    x=k.recvfrom(10240)
    print()
    os.system("tput setaf 3")
    width = os.get_terminal_size().columns
    print(x[0].decode().center(width))
    os.system("tput setaf 7")
t1=threading.Thread(target=send)
t2=threading.Thread(target=recv)
t1.start()
t2.start()

		
		
		
