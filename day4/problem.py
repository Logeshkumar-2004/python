num1 = int(input("enter a value of num1 ="))

num2 = int(input("\n enter a value of num2 ="))
op = (input(" \n select operation  +, -, *, /, //, %, ** => \n"))

print(num1,op,num2)

if op == '+':
   print(num1 + num2)

elif op == '-':
   print(num1 - num2)

elif op == '*':
   print(num1 * num2)

elif op == '/':
   print(num1/num2)

elif op == '//':
   print(num1 // num2)

elif op == '%':
   print(num1 % num2)

elif op == '**':
   print(num1 ** num2)


else :
   print(" Invalid operation")
