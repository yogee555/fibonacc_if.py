# Fibonacc
n = int(input("enter the number: "))
a=0
b=1
if n<0:
    print("in correct input")
elif n==0:
    print(a)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(b)