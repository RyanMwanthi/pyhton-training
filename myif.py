marks =80

if marks>70:
    #runs if value is true if not true (.....else)
    print(False)
    print("You have passed")
else:
    #it is executed when the boolean id false
    print(False)

print("Run either way")

#ELIF-works with multiple conditions
#find the grade of the marks below
# >=70 - A
# <70 and >=60-B
#<60 and >=50 - C
# <50 and >=40 -D
# <40 - E

marks=90
if marks>=70:
    print("A")
elif marks < 70 and marks>= 60:
    print("B")
elif marks< 60 and marks>=50:
    print("C")
elif marks< 50 and marks>=40:
    print("D")
else:
    print("E")

#input nuber see if its above 50 and print pass else fail
# used nested if to solve the issue below

number=int(input("Enter number:"))
print(number)
if 0<= number <=100:
     if number>=50:
         print("pass")
     else:
         print("fail")
else:
    print("invalid")        

  



    

