#1
b=(int(input("enterb:")))
h=(int(input("enterh:")))
area=b*h/2
print(area)

#3 phone number
phone_number = input("Enter number: ")

if phone_number.startswith("+254"):
    print("Valid format.")
else:
    if phone_number.startswith("07"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("71"):
        phone_number = "+254" + phone_number[1:]
    elif phone_number.startswith("254"):
        phone_number = "+254" + phone_number[3:]
    elif phone_number.startswith("01"):
        phone_number = "+254" + phone_number[1:]
    else:
        print("Invalid phone number.")
        exit()

    print(phone_number)

#4 Email
email = str(input("enter the email: "))
email.strip().lower()
if "@" and "." in  email[1:]:
    print("Correct format", email)
else:
    print("invalid email")


#5
x=80
y=70
z=60
print(max(x,y,z))

#7

marks=int(input("Enter Marks:"))
if (marks>=79):

    print("A:")
elif (marks < 79) and (marks>= 60): 
     print("B:")
elif (marks< 60) and (marks>=50):

    print("C:")
elif (marks< 50) and (marks>=40):
    print("D:")
else:
    print("E:")

 #10
prods=[['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
print(type(prods))
  
sum=int(prods[0][2])+int(prods[1][2])+int(prods[2][2])+int(prods[3][2])
print(sum)

#15
basic_salary=int(input("Enter_Salary:"))
benefits=int(input("Benefits:"))
gross_pay=(benefits+basic_salary)


if 35000<= gross_pay <=39999:
    NHIF=950
    netpay=(gross_pay-NHIF)
    print(netpay)
elif 60000<= gross_pay<=69999:
    NHIF=1200
    netpay=(gross_pay-NHIF)
    print(netpay)
elif 90000<=gross_pay<=99999:
    NHIF=1600
    netpay=(gross_pay-NHIF)
    print(netpay)

#password
password = "admin@123"
attempts = 4
while attempts > 0:
    user_passcode = input("Enter the password:")
    if user_passcode == password:
        print("Access grandted.")
        break
    else:
        attempts-=1
        print("Incorrect password.Attempts left:",attempts)
        if attempts == 0:
            print("Account blocked.")



# Figure out your age
import datetime
currentDate = datetime.datetime.now()

deadline= input ('Enter date of birth (mm/dd/yyyy):')
print (deadline)

