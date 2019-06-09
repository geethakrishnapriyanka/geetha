a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("add operation:1","sub operation:2","mul operation:3","div operation:4")
c=int(input("enter the operation:"))
if(c==1):
    d=a+b
    print("the sum is",d)
elif(c==2):
    d=a-b
    print("the subtraction is",d)
elif(c==3):
    d=a*b
    print("the multiplicaton is",d)
elif(c==4):
    d=a/b
    print("the division is",d)
else:
    print("enter the numbers between 1 to 4")
