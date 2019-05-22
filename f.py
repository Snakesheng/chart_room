def fun():
    print("子进程开始执行")
    sleep(3)
    print("子进程执行完毕")

p = fork()

if p == 0:
    fun()
    os._exit()
else:
    sleep(2)
    print("父进程干点事")
    wait()

...