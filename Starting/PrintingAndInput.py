#Methods in string
name = "Vijay Dahiya"

#convert cases
print(name.upper())
print(name.lower())

#check index
print(name.find('V')) #return 0
print(name.find('S')) #return -1
print(name.find('ija')) #return 1
print(name.find("ijae")) #return -1

#replace
print(name.replace("Dahiya","Jatt"))

#check if present using "in" keyword
print("V" in name) #return true

#operator
i=5
print(5+2)
print(10/3)
print(10//3)
print(10%3)
print(5**2)

i += 2
print(i)
i *= 2
print(i)
i /= 2
print(i)
i//= 2
print(i)

#comparison
print(i>2)
print(i>=3)
print(2==3)
print(3!=2)

#logical operator
print(2>3 or 4>3)
print(1>3 and 1<3)
print( not 2>3)

#conditional statements
age = 16
if age>20 :
    print("You are good to go.")
    print("Best of luck.")
elif age==16 :
    print("Hey")
else :
    print("Bey")

print("Thank you")