# Python Variables

"""
Variable is a name that is used to refer to memory location. Python variable is 
also known as an identifier and used to hold value.
"""

#Creating Variables in Python
str1="My name is Hancie Phago"
print(str1)

int1=70
print(int1)

str2="Python"
str3="is"
str4="Awesome"
print(str2,str3,str4)

#Casting in Python
x=str(3)
y=int(3)
z=float(5)

print(x)
print(y)
print(z)


#Assign Multiple Values

a,b,c="Hancie", "Nitesh", "Bardan"
print(a)
print(b)
print(c)

#One Value to Multiple Variable

q=w=e="Hello!"
print(q)
print(w)
print(e)

# Unpack a Collection

# If you have a collection of values in a list, tuple etc. Python 
# allows you to extract the values into variables. 
# This is called unpacking.

fruits=["Apple","Orange","Mango"]
x=fruits
print(x)


# Global Variables

# Variables that are created outside of a function (as in all of the examples above)
#  are known as global variables. Global variables can be used by everyone,
#  both inside of functions and outside.

str5="Hancie"

def myfunc():
    print("My name is " +str5)


myfunc()


#The Global Keyword

def globalexample():
    global x
    x="Fantastic"

globalexample()

print("The python is "+x)



