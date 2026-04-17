#Ask for the user's input

cash1 = int(input("Enter first balance: "))
op = input("Enter operator: (+, -, *, /, %): ")
cash2 = int(input("Enter the second balance: "))

#Perform the calculation based on the operator provided from the user

if op == "+":
     print(cash1 + cash2)

elif op == "-":
    print(cash1 - cash2)

elif op == "*":
    print(cash1 * cash2)

elif op == "/":
    print(cash1 / cash2)

elif op == "%":
    print(cash1 % cash2)

else:
    print("Wrong operator, please try again")