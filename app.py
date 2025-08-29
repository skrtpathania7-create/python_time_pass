course="programming python"
print(len(course))
print(course[0])
print(course[2:9])
a=3
b=6
print(a+b)
a,b,c="quick","red","fox"
print(a+b+c)
a,b=6,"hello"
print(a,b)
a="qwerty"
for x in a :
    print(x)
a="thequickredfox"
print("dog" in a)
a="the,lazydog jumps"
print(str.capitalize(a))
a="three"
print(a.center(20,"9"))
a="THEree"
print(a.swapcase())
a="123"
b="²3"
c="Ⅳ"
d="½"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(round(3.4))
print(abs(-2.4))
temperature = 50
if temperature > 30:
    print("its warm")
    print("drink water")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")
print("done")
age=11
message = "eligible" if age >= 18 else "not eligible"
print(message)
temperature=22
message = "eligible" if temperature >= 32 else "not eligible"
high_income = "false"
good_credit = "true"
student = "false"
if (high_income or good_credit) or not student:
    print("eligible")
else:
    print("not eligible")

year=int(input("enter the year: "))
if (year % 100 == 0 and year % 400 == 0):
    print("entered year {} is leap year".format(year))
elif(year % 4 == 0 and year % 100 != 0):
    print("entered year {} is a leap year".format(year))
else:
    print("entered year {} is not a leap yaer".format(year))

num1=float(input("enter a number: "))
if num1>0:
    print("positive")
elif num1<0:
    print("negative")
else:
    print("zero")
a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

operator = input("enter an operature (+ - * /)")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")
i=1
while i<6:
    print(i)
    i+=1

i=1
while i<11:
    print(i)
    i+=1
i=2
while i<=20:
    print(i)
    i+=2
i=1
while i<=20:
    if i%2==0:
        print(i)
    i=i+1

n=int(input("enter a number:"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1
i=1
total=0
while i<=n:
    total=total+i
print("sum=",total)
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")




