import math
num=input("Enter Student ID: ")
fullname=input("Enter name: ")
caddress=input("Enter address: ")
email=input("Enter email: ")
phone=input("Enter phone: ")


print("Your Student ID is: {} ".format(num))
print("Your name is: {}".format(fullname))
print("Your address is: {}".format(caddress))
print("Your email is: {}".format(email))
print("Your phone is: {}".format(phone))

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

num3=num1+num2
num4=num1/num2
num5=num1*num2
num6=num1-num2
num7=num1**num2
num8=math.pow(num1, num2)

print("The result is: {}".format(num3))
print("The result is: {}".format(num4))
print("The result is: {}".format(num5))
print("The result is: {}".format(num6))
print("The result is: {}".format(num7))
print("The result is: {}".format(num8))

class Calculator():
    def sum(self, num1, num2):
        return num1+num2

    def sub(self, num1, num2):
        return num1-num2


c1=Calculator()
result=c1.sum(4,5)
sub=c1.sub(5,2)
print("Sum: {}".format(result))
print("The sub is: {}".format(sub))



