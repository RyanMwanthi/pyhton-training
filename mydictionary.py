#Dictionaries are values defined using key : value pairs that you access using a akey instead of an index

Person = {"name":"John Doe", "age":30,"location":"Nairobi", }
print(Person["age"])
t= "name" in Person.keys()

print(t)
print(type(Person))

voters={
          "1000":{"name":"john","city":"nairobi"},
          "2000":{"name":"ken","city":"machakos"},
          "3000":{"name":"dave","city":"nakuru"}}

#when printing, use (voters(thid id the name of the variable tjhat you have created[""])


print(voters["3000"])


task_list =23,"Jane",(560), ["Lesson","Math",{"Currency" :"KES"}],987,(76,"John")

ks=task_list[3][2]
print(ks["Currency"])
 
fv=task_list[2]
print(fv)

m=task_list[3][1]
print(m)

print(type(task_list))
 
nm=task_list[4]
print(nm)

task_list5=str(task_list[-2])
task_list5=task_list5[::-2]
print(task_list5)


num="987"
mun=num[::-1]
print(mun)