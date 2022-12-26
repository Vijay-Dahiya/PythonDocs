#Calculator
first = input("Please enter a number : ")
operator = input("Please choose a operator(+,-,*,/) : ")
second = input("Please enter second number : ")

if operator=='+' :
    print(int(first)+int(second))
elif operator == '-' :
    print(int(first)-int(second))
elif operator == '*':
    print(int(first)*int(second))
elif operator == '/':
    print(int(first)/int(second))
else :
    print("Please enter a valid input.")
