# Open a File and Read
f=open("file.txt")
print(f.read())

# Read Lines
# You can return one line by using the readline() method:
f=open("file.txt")
print(f.readline())

f=open("file.txt")
for x in f:
    print(x)


# Close Files
# It is a good practice to always close the file when you are done with it.
f=open("file.txt")
print(f.read())
f.close()


# Append the file
f=open("file.txt", "a")
f.write("My best friend name is Nitesh Hamal")
f.close()

f=open("file.txt")
print(f.read())
f.close()