from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p = Process(target = tm,name = "Tedu")

#　子进程随父进程退出
p.daemon = True

p.start()
print("Name:",p.name)  #　获取名称
print("PID:",p.pid)    # 获取ＰＩＤ
print("is Alive:",p.is_alive()) # 是否在生命周期




