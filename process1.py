#　multiprocess 示例
import multiprocessing as mp
from time import sleep

a = 1

# 子进程函数
def fun():
    print("子进程开始执行")
    global a
    print("a = ",a)
    a = 10000
    sleep(3)
    print("子进程执行完毕")

# 创建进程对象
p = mp.Process(target = fun)

#启动进程
p.start()

sleep(2)
print("父进程干点事")

#　回收进程
p.join()

print("parent a :",a)

