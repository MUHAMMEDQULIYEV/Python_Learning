import random

prompt=input("Enter your name: ")
print (f"Hello {prompt}")



print("\n")



hours=float(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
print(f"Pay {round(hours*rate,2)}")


celc=float(input(" Enter a Celcius Temperature "))

print(f"{9/5*celc+32} fahrenheit")

x=23


if x>10:
    pass
inp=input("Enter a Fahrenheit temperature ")
try:
    fahr=float(inp)
    celc=((fahr-32)/9*5)
    print(celc)
except:
    print("Please Enter a Number")


for _ in range(10):
    """random.random give us a list of number between 0 and 1"""
    y=random.random()%100
    print(y)
for _ in range(10):
    """random.random give us a list of number between 0 and 1"""
    y=random.randint(1,10)
    print(y)


ls=[1,2,3,4,5]
print(random.choice(ls))


print(dir(str))
s = "hello world"
letters = list(s)          # ['h','e','l','l','o',' ','w','o','r','l','d']
joined = "".join(letters)  # "hello world"
