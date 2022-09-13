# Python String

"""Python string is surrounded by either single quotation marks or double quotation marks."""

# 'hello' is same as "hello"

#Assign string to the variable

str1="Hello Python!"
print(str1)

# Multi-Line String

str2="""Computer is a electronic machine which process
the data and give us result in the form of output"""

print(str2)


#String are Arrays

arr="Hello!"
print(arr[1])


#Looping through Strings

for x in "Apple":
  print(x)


#String Length

# To get the lenght of string, use len() function

len1="Hello World!"
print(len(len1))


# Check String

#To check certain word or phrase is present in the string, we can use in keyword

check="Python is awesome"

print("is" in check)

if "awesome" in check:
    print("Wow, I found awesome word")


# Check Not String

chk="Python is a programming language"
print("hancie" not in chk)

if "hancie" not in chk:
    print("Hancie is not found!")


# Slicing in String

a="My name is Hancie"
print(a[0:4])


# Python Modifying Strings

up="Hello!, My name is Hancie"
print(up.upper())

down="HELLO!, MY NAME IS HANCIE PHAGO"
print(down.lower())


# Replace String

# The replace() method replaces a string with another string:

replace1="Hancie Phago"
print(replace1.replace("H", "N"))

# String Concatenation

x="Hello"
y="Hancie"
z=x+y
print(z)

x="Hello"
y="Hancie"
z=x+" "+y
print(z)


