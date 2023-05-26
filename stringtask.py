name="  JOHn ."
name=name[2:6].lower()
print(name)


sentence_one="The Dog Breed is German Shepherd"
print(sentence_one[8:23])
print(sentence_one[-24:23])
sentence_two="Defeat for the Clinton forces, this was her moment of truimph"
print(sentence_two[15:29])
print(sentence_two[-46:29])


dog="The lazy dog ran so fast it hit the wall"
print(dog)
dog=dog.replace(("The lazy dog ran so fast it hit the wall"),("The lazy dog; ran so fast; it hit the wall"))
print(dog)
fast=dog.split(";")
print(len(fast))
print(fast)

s="foo"
t="bar"
print("barf" in 2 *(s+t))

s='foobar'
s=s[::-1]
print(s)
