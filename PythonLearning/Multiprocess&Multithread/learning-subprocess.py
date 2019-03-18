# -*-coding:UTF-8-*-
import subprocess

print('$ nslookup www.python.org')
# print('nslookup')
r = subprocess.run(['nslookup', 'www.python.org'])
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gb2312')) #防止显示乱码
print('Exit code:', r.returncode)
# print('Exit code:', p.returncode)



