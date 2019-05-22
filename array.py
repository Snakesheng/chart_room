from multiprocessing import Process, Array

# 　创建共享内存
# 　共享内存开辟５个整型列表空间
# shm = Array('i',5)

# 　共享内存初始化数据[1,2,3]
# shm = Array('i', [1, 2, 3])

#　字节串
shm = Array('c',b'hello')

def fun():
    # 　共享内存对象可迭代
    for i in shm:
        print(i)
    #　修改共享内存
    shm[0] = b'H'


p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i, end=' ')

# 通过ｖａｌｕｅ属性访问字节串
print(shm.value)
