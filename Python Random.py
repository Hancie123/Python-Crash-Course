from random import random, randrange
from array import array


# num=random.random()
# num=num*100
# print(num)
#
#
# num=random.randint(0,1000)
# num=num*1000
# print(num)
#
# myList=["H","T"]
# coin=random.choice(myList)
# guess=input("Enter head or tail: ").upper()
#
# if guess==coin:
#     print("You win")
#
# else:
#     print("Bad Luck")
#
# if coin=="H":
#     print("It has Head")
# else:
#     print("It has tail")
#
# myList=[1,2,3,4,5]
# shuffle=random.choice(myList)
# guess=int(input("Enter number between 1 to 5: "))
#
# if guess==shuffle:
#     print("You have won")
# elif guess>shuffle:
#     print("You have pick greater number")
#     again=int(input("Enter number again: "))
#     if again==shuffle:
#         print("Correct")
#     else:
#         print("You Loose")
# elif guess<shuffle:
#     print("You have picked smaller number")
#     again2=int(input("Enter number again: "))
#     if again2==shuffle:
#         print("You have won")
#     else:
#         print("You Loose")
#
#
# print(random())
# print(randrange(10))
# print(randrange(500,1000))

#Looping
# a=array('i',[])
# for i in range(0,24):
#     a.append(randrange(17,23))
#
#
# print(len(a), end=" ")
# print(min(a))
# print(max(a))
# print(sum(a)/len(a))
#
# tmp=input("Enter age to find: ")
# tmp=int(tmp)
#
#
# count=a.count(tmp)
# index=a.index(tmp,0,23)
# if count>0:
#     print("{} found {} time(s) at {}".format(tmp,count,index))
#     if tmp in a:
#         print(a.index(tmp))
# else:
#     print("{} not found".format(tmp))

















al = ['a','d','e','c','b']
al.sort(reverse=True)
print('List in Descending Order: ', al)

al.sort()
print('List in Ascending Order: ', al)

arr = array('i',[5,4,7,8,2,3])
temp = 0;

print("Elements in original array: ");  # printing the original array
for i in range(0, len(arr)):
    print(arr[i]),

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):  # comparing the elements using nested for loop
        if (arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];  # swapping the elements
            arr[j] = temp;

print();

print("Array sorted in ascending order: ");
for i in range(0, len(arr)):
    print(arr[i]),


arr1=array('i',[5,7,1,2,2,4,4,5])
tmp=input("Enter number: ")
tmp=int(tmp)
count=arr1.count(tmp)
if count>0:
    print("")
print(arr1)


