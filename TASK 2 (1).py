print("------simple calculator------")

#user input
number1 = float(input("Enter number1 : "))
number2 = float(input("Enter number2 : "))
operation = input("Enter operation[+ , - , * , / , %] : ")

#calculation
if operation == "+":
   result = number1 + number2
elif operation == "-":
   result = number1 - number2
elif operation == "*":
   result = number1 * number2
elif operation == "/":
   if number2 == 0:
       result = "Error! Division by zero."
   else:
       result = number1 / number2
elif operation == "%":
   result = number1 % number2
else:
   result = "Invalid operation."

#output
print("Result: ",result)
