#factorial

x=int(input("enter the number:"))

f=1
if (x<0):
    print("can't find factorial")
elif (x>0):
    for i in range(1,x+1):
        f=f*i
    print(f)


#word count
f=open("exam.txt","r")
print(f.read())



