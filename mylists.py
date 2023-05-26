week=["Monday","Tuesday","WEDNESDAY","Thursday","Friday"]
today=week[1]
print(today)
print(len(week))
mylist=week+week
print(mylist)
mylist1=week*4
print(mylist1)
day4="wednesday".upper() in week
print(day4)
day4=str(day4)
day4=day4[0]
print(day4)
del week[0]
print(week)
week[2]="Thur"
print(week)
week.append("Saturday")
print(week)

trainees=["John",[2,["James","Mary"]]]


two=trainees[1][0]
print(two)

jamo=trainees[1][1][0]
print(jamo)


trainees.append("56")
print(trainees)

trainees[1][0]=8
print(trainees)

trainees[1][1].insert(1,"Mike")
print(trainees) 
  
print(len(trainees))


del trainees[0]
del trainees[0][1][-1]
print(trainees)