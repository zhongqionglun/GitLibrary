# -*-coding:UTF-8-*-

"""
paramiko
def function1: ssh connection use username and password ,sshclient.exec_command()
def function2: ssh connection use private_key, sshclient.transport().open_session().exec_command()
"""

import paramiko
import StringIO


def function1():
    clientssh = paramiko.SSHClient()  # 创建客户端
    clientssh.load_system_host_keys()  # 读取hosts文件
    clientssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    clientssh.connect(hostname=hostname, port=port, username=username, password=password)  # 连接服务器
    stdin, stdout, stderr = clientssh.exec_command(execmd1)  # 执行命令
    stdin.write("Y")
    print(stdout.read())  # 获取命令执行结果
    clientssh.close()  # 关闭连接


def function2():
    paramiko.util.log_to_file('paramiko.log')
    fid = open('C:\Documents and Settings\Administrator\.ssh\id_rsa', 'r')
    rsastring = fid.read()
    keyfile = StringIO.StringIO(rsastring)
    private_key = paramiko.RSAKey.from_private_key(keyfile)
    ssh = paramiko.SSHClient()  # 创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
    ssh.connect(hostname, port, username, private_key)  # 连接服务器,公钥已经加入到服务器的authorized_keys文件中
    ssh_session = ssh.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(execmd2)  # 执行命令
        print(ssh_session.recv(1024))  # 获取命令结果
    ssh.close()  # 关闭连接


if __name__ == '__main__':
    hostname = "192.168.88.101"
    port = 22
    username = "root"
    password = "123456"
    execmd1 = "free"
    execmd2 = "df"
    function1()
    function2()
