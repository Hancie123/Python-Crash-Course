# print(help(tuple))
import sys
from array import array

# list1=[5,4,6,7,8]
# # tup1=(1,2,3,4,5,6)
# tup1=tuple(list1)

# arr=array('i',[5,7,8,4,5])
# tup1=tuple(arr)
# tup1=4,6,7,8,4,5
# print(tup1)
# print(tup1[5:])
# print(tup1[0:len(tup1):1])
# print(tup1[::-1])
# print(tup1[-3])
# print(type(tup1))
# print(id(tup1))
# print(len(tup1))
# print(sys.getsizeof(tup1))


tup1=(2,5,6,8,9,4,5,6,7,8,1)
print(tup1.count(4))
print(tup1.index(1,0,len(tup1)))
print(tup1)
