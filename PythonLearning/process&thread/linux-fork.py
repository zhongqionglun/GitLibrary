# -*- coding: utf-8 -*-
import os

"""
learning the fork() of os module
"""

print("Process (%s) start..." % os.getpid())
pid = os.fork()
if pid == 0:
    print("I am child process (%s) and my parent is (%s)..." % (os.getpid(), os.getppid()))
else:
    print("I (%s) just created a child process (%s)..." % (os.getppid(), pid))
