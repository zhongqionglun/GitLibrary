# -*-coding:UTF-8-*-

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

"""
auth:zhongqionglun
time:2019/3/18
"""

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def get_task():
    return task_queue


def get_result():
    return result_queue


def test():
    # 把两个队列都注册到网络上，callable参数关联了Queue对象
    BaseManager.register('get_task', callable=get_task)
    BaseManager.register('get_result', callable=get_result)

    # 绑定端口5000，设置验证码‘abc’
    manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task()
    result = manager.get_result()

    # 放任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d ...' % n)
        task.put(n)

    # 从result队列取出结果
    print('Try get results ...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result is: %s' % r)

    # 关闭各个线程
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    freeze_support()
    test()
