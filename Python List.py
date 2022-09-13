# List

#Join the two list
a=["Hancie", "Nitesh"]
b=["Ajaya", "Aveshesh"]
c=a+b
print(c)

#Alternative use extend method
a.extend(b)
print(a)

fruits=["Apple", "Banana", "Mango","Orange"]  # List Data Types

for x in fruits:
    print(x)

#Access the list
print(fruits[1])

# Add an elements in List
fruits.append("Pineapple")  #Append method
print(fruits)



#Insert an element
fruits.insert(1, "Guava")
print(fruits)

#Remove item from the list
fruits.remove("Guava")
print(fruits)

#Reverse
fruits.reverse()
print(fruits)

#Short the list
fruits.sort()
print(fruits)

# Clear the list
fruits.clear()
print(fruits)

