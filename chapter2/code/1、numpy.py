import numpy as np

a1 = np.arange(9).reshape(3,3)
print('1.创建一个3×3的二维数组,值域为0到8:\n',a1)

a2 = np.arange(2,4*10+2,4)
print('2.给出起点2,长度10和步长4,创建一个numpy数组:\n',a2)

a3= np.random.rand(10,10)
print(f'3.最大值:{a3.max()},最小值:{a3.min()}')

a = np.array([[4,5],[6,7]])
b = np.array([[1,5],[3,4]])
print('计算a和b的普通乘法:\n',a*b)
print('计算a和b的矩阵乘法:\n',np.dot(a,b))
print('a的转置:\n',a.T)
print('b的转置:\n',b.T)
print('a沿列累计总和:\n',a.cumsum(axis=0))
print('b沿列累计总和:\n',b.cumsum(axis=0))
print('a+b:\n',a+b)
print('横向合并a和b:\n',np.hstack((a,b)))
print('纵向合并a和b:\n',np.vstack((a,b)))
print('将a纵向分为两部分:\n',np.vsplit(a,2))
print('将b横向分为两部分:\n',np.hsplit(b,2))

a5 = np.arange(32).reshape(8,4)
print('5.0-31这32个数字中分成8行4列:\n',a5)

a6 = np.linspace(1,2,3)
print('6.在1和2之间（包括1和2）分成等值的3份输出:\n',a6)

a7 = np.eye(9)
print('7.输出行列都为9的单位矩阵:\n',a7)

for i in np.linspace(1,2,3):
    print(i)

a9 = np.linspace(0,2,6)
print('9.创建一个大小为6的向量,值域为0到2:\n',a9)

a10 = np.zeros(10)
print('10.创建大小为10的,值为0的向量:\n',a10)

a11 = np.sort(np.random.randint(0,10,11))
print('11.创建一个大小为10的向量,并排序:\n',a11)

a12 = np.random.randint(0,10,(4,4))
print('12.创建一个4*4数组,使用索引的方式获取第二行第一列和第三行第二列的数据:\n',a12[1,0],a12[2,1])

print('13.使用切片的方式获取上题中数组的前2行第2,3列的数:\n',a12[:2,1:3])