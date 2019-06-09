l=['a','c','abcd','abc','ab','xyzaef']
n=int(input("enter integer"))
a=list()
for i in l:
    if(len(i)>n):
      print(i)
      a.append(i)
print(a)
