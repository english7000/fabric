#coding=utf-8
#！/usr/bin/env python3


import paramiko
import os

class server(object):
    def __init__(self):
        self.ssh = ''
        self.trans = ''


    def initial(self):
        client_info = {}
        with open('../cfg/client_info', 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    host,user_name,passwd = line.split(':')
                    client_info[host]=(user_name,passwd)
        return client_info

    def conn(self, user_name, ip, passwd, port =22):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(username=user_name, hostname=ip, password=passwd, port=port)
        self.ssh =ssh

        transfer = paramiko.Transport((ip, port))
        transfer.connect(username=user_name, password=passwd)
        self.sftp = paramiko.SFTPClient.from_transport(transfer)


    def user_interface(self,client_info):
        for i in client_info.keys():
            print(i,'\n')
        user_choose = input('>>:')
        if user_choose in client_info.keys():
            return user_choose
        else:
            print('Wrong input!')


    def exec_command(self):
        print('Please input the command (q to quit)')
        command = input('>>:').strip()
        if command == 'q':
            return 1
        elif command.startswith('cd'):          #paramiko cd问题，待解决
            pass

        elif command.startswith('put') or command.startswith('get'):
            self.transfer(command)
        else:
            stdin,stdout,stderr = self.ssh.exec_command(command)
            print(stdout.read().decode(), stderr.read().decode())


    def transfer(self, command):
        if command.startswith('put'):
            local_path = command.replace('put ','')
            file_name = command.replace('put ','').split('/').pop()
            self.sftp.put(local_path,file_name)
        elif command.startswith('get'):
            stdin,stdout,stderr = self.ssh.exec_command('pwd')
            pwd = stdout.read().decode().strip('\n') +'/'
            path = command.replace('get ',pwd)
            print(path)
            file_name = command.replace('get ','').split('/').pop()
            self.sftp.get(path,file_name)







