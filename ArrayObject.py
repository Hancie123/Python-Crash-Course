import array

import sys

# declare an array
nums=array.array('i',[5,6,2,8,9])
print(nums)
print(type(nums))
print(id(nums))
print(sys.getsizeof(nums))
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[3])
print(nums[-1])

print(nums[0:5])
print(nums[0:10])
print(nums[0:10:1])
print(nums[5:0:-1])
print(nums[:])
print(nums[:5])
print(nums[::1])


nums[2]=5
print(nums)

del nums[4]
print(nums)

nums.append(11)
print(nums)

# print(dir(array.array))

print(help(array.array))



num=array.array("i",[5,6,2,8,9])
print(num)
print(id(nums[0]))
num.append(5)
print(num)


var1=int(input("Enter any number: "))
var2=input("Do you want more?")

if var2=='Y':
    var3=int(input("Enter number: "))
    num.append(var3)

elif var2=='N':
    print("Thank you!")

num.append(var1)
print(num)