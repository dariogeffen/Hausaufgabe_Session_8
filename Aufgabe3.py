number1 = input("Insert the first number: ")
operation = input("Insert the arithmetic operation: ")
number2 = input("Insert the second number: ")

try:
    int(number1)
except:
    print ("The first number is not a number!")
try:
    int(number2)
except:
    print ("The second number is not a number!")

if operation =="+":
    print ("The result is:", int(number1) + int(number2))
elif operation =="-":
    print ("The result is:", int(number1) - int(number2))
elif operation =="*":
    print ("The result is:", int(number1) * int(number2))
elif operation =="/":
    print ("The result is:", int(number1) / int(number2))
else:
    print ("Please insert a valid arithmetic operation (i.e. +,-,/,*")