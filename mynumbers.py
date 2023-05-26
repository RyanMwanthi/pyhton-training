import math


x=2
y=5
print(x*y)

print(y%x)

x=34
y=7
print(34//y)

temp=56.8926
temp=temp.__round__().__int__()
print(type(temp))
print(temp)

num=56.8926
num=(round(56.8926,2))
print(num)

temp=56.8926
temp=round(temp,3)
temp=(round(56.8926,3))
print(temp)

temp=56.8926
temp=(round(56.8926,0))
print(temp)
temp=56.8926
temp=temp.__str__()
print(type(temp))
print(temp[3:7])
temp=temp[3]+"."+temp[4:7]
print(temp)

num = input("Enter value:")
print(num)