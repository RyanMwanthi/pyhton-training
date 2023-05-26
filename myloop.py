#loop is used to get values from inside a data structure like a list or a tuple
#reapeating something over and over
#store the values in a list then loop through the same list
#in the body of the loop,you can execute anyother code(it can be if , indexing slicing operations or methods)
#or even another loop


#1.create a list

lst=range(0,10)
lst_1=list(lst)

for i in lst_1:
    if i%3==0:

     print(i)
    #gives a value one at a time
    #i will have a different value thus print("i is",i)

lst_3=["Nairobi","Mombasa","Nakuru","Eldoret"]
#display cities that only have letter "a"
res=[]
for letr in lst_3:
    if "a" in letr:
        res.append(letr) 
      
print(res)     

 # make an empty list then add by appending the variable above(append(letr))     

