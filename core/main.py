#coding=utf-8
#！/usr/bin/env python3

import os,sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir)
from core import server
import threading

with open('../cfg/max_session_allow','r') as f:
    n = f.readline()
n = int(n)
print('max session:',n)

semaphore = threading.BoundedSemaphore(n)

def run():

    semaphore.acquire()
    ser = server.server()
    client_info = ser.initial()
    # print(client_info)
    ip = ser.user_interface(client_info)
    # print(ip,type(ip))
    print(client_info[ip])
    ser.conn(client_info[ip][0], ip, client_info[ip][1])

    while True:
        res = ser.exec_command()
        if res =='1':
            break

    semaphore.release()

run()