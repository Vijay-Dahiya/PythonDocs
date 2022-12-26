#Range
numbers = range(5)
i=1
while i<= 5:
    print(i * "*")
    i+=1

for it in range(5):
    print(it)

marks= [90,98,78,"maths"] #use []
print(marks)
print(marks[0:2])
print(marks[2])

for score in marks :
    print(score)

marks.append(89)
marks.insert(1,99)

print(99 in marks)
print(len(marks))
x=1
while x<len(marks) :
    print(marks[x])
    x += 1

marks.clear()
print(marks)


#Immutable list

mark= (98,97,97,97,89) #use ()
print(mark.index(97))
print(mark.count(97))

#sets

markset= {89,90,99,99} #set use {}

for score in markset :
    print(score)

dictonry = {"english" : 99,"chemistry" : 97 }
print(dictonry["chemistry"])
dictonry["physics"]= 100
print(dictonry["physics"])
dictonry["physics"]= 99.5
print(dictonry["physics"])





