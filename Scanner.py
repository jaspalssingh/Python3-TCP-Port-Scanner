#!/usr/bin/python3

import socket
import sys
import threading

usage = "python3 Scanner.py TARGET START_PORT END_PORT "

if(len(sys.argv)<=2):
    print("Tool Usage:"+usage)
    sys.exit()

print("-"*70)
print("Python Simple Port Scanner")
print("-"*70)

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution Error")
    sys.exit()
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print("Scanning target",target)
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1);
    # We are using connect_ex so that it doesn"t terminate the program if port is not open
    conn = s.connect_ex((target, port)) 
    if(not conn):
        print("Port {} is OPEN".format(port))
    s.close()
for port in range(start_port,end_port):
    thread = threading.Thread(target = scan_port, args =(port,))
    thread.start()

