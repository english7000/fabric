#coding=utf-8
#！/usr/bin/env python3


import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='127.0.0.1', username='karl_', password='vbvbvbvb', port=6969)
stdin,stdout,stderr = ssh.exec_command('pwd')
print(stdout.read())