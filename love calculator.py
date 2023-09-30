
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name3=name1.lower()+name2.lower()

t=int(name3.count("t"))
r=int(name3.count("r"))
u=int(name3.count("u"))
e=int(name3.count("e"))

true_word= t+r+u+e

l=int(name3.count("l"))
o=int(name3.count("o"))
v=int(name3.count("v"))
e=int(name3.count("e"))

love_word= l+o+v+e

a= str(true_word)
b= str(love_word)

result= int(a+b)

if result <10:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result>90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result<50 and result >40:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")