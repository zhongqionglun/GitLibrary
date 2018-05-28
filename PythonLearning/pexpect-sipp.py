# -*-coding:UTF-8-*-


import pexpect


def function1():
    try:
        ssh = pexpect.spawn("ssh root@172.29.1.89")
        res = ssh.expect('Are you sure you want to continue connecting (yes/no)?','password:')
        if res == 0:
            ssh.sendline('yes')
            ssh.expect('password:')

        if res == 1:
            ssh.sendline('123456')
    except Exception as e:
        print('ssh root@172.29.1.89 Fail! %s' % e)
        exit()


if __name__ == '__main__':
    function1()
