
n1=int(input("print stars:"))
n2=int(input())
new = bool(n2)
if new==True:
    for i in range(1,n1+1):

        for j in range(1,i+1):
            print("*",end="")
        print()
elif new==False:
    for i in range(n1,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()