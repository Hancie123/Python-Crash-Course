# Data Type in Python

# String Data Types
str1="Hello World"  

# Numeric Data Types
int1=25 #Int Data Types
a=2.5  #Float Data Types
b=1+3j  #Complex Data Types

# Sequence Data Types
c=["Hancie", "Nitesh","Bardan"]   #List Data Types
d=("Hancie", "Nitesh","Bardan")   #Tuple Data Types
e=range(6)                        #Range Data Types


# Mapping Data Types
f={"name": "Hancie Phago", "Age": 20}  #Dict Data Types

# Set Data Types
g={"Hancie", "Nitesh","Bardan"}   #Set Data Types
h=frozenset({"Hancie", "Nitesh","Bardan"})   #Frozen Data Types

#Boolean Data Types
i=True   #Boolean Data Types

#Binary Data Types
m=b"Hello"
print(m)
j=bytearray(5)  #ByteArray Data Types
print(j)
k=memoryview(bytes(5))  #MemoryView Data Types
print(k)

# None Data Types
l=None  #None Data Types
print(l)


print(type(str1))
print(type(int1))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))


class Student():
    pass

sid=Student()
print(type(sid))