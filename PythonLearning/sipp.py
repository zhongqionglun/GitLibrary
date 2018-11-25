# -*-coding:UTF-8-*-


import paramiko
import io


class SshModule:
    def __init__(self, hostname, port, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp = None
        self.ssh.connect(hostname, port, username, password)
        self.sftp = self.ssh.open_sftp()

    def ssh_exec_command(self, comm):
        stdin, stdout, stderr = self.ssh.exec_command(comm)
        stdin.write("Y")
        print(stdout.read())
        self.ssh.close()

    def upload_file_to_remote(self, localpathfile, remotepathfile):
        self.sftp.put(localpathfile, remotepathfile)
        return

    def download_file_from_remote(self, remotepathfile, localpathfile):
        self.sftp.get(remotepathfile, localpathfile)
        return


if __name__ == '__main__':
    hostname = "192.168.3.3"
    port = 22
    username = "root"
    password = "123456"
    cmd = "sipp/sipp -i 192.168.3.3 -sf /root/sipp/uac.xml -inf /root/sipp/call.csv 192.168.3.2:5060  -t -u -m 1"
    paramiko.util.log_to_file('paramiko.log')
    sshconnect = SshModule(hostname, port, username, password)
    sshconnect.ssh_exec_command(cmd)

