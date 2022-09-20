import random

num=random.random()
num=num*100
print(num)


num=random.randint(0,1000)
num=num*1000
print(num)

myList=["H","T"]
coin=random.choice(myList)
guess=input("Enter head or tail: ").upper()

if guess==coin:
    print("You win")

else:
    print("Bad Luck")

if coin=="H":
    print("It has Head")
else:
    print("It has tail")

myList=[1,2,3,4,5]
shuffle=random.choice(myList)
guess=int(input("Enter number between 1 to 5: "))

if guess==shuffle:
    print("You have won")
elif guess>shuffle:
    print("You have pick greater number")
    again=int(input("Enter number again: "))
    if again==shuffle:
        print("Correct")
    else:
        print("You Loose")
elif guess<shuffle:
    print("You have picked smaller number")
    again2=int(input("Enter number again: "))
    if again2==shuffle:
        print("You have won")
    else:
        print("You Loose")





