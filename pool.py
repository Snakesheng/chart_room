"""
进程池原理示例
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件
def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#　创建进程池
pool = Pool(6)

#　向进程池添加事件
for i in range(20):
    msg = "Hello %d"%i
    r = pool.apply_async(func=worker,args=(msg,))

#　关闭进程池
pool.close()

#　回收进程池
pool.join()

print(r.get()) #　获取事件函数返回值















