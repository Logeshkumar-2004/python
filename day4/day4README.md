Day 4: if, else, elif – Conditional Statements
🔹 1. Basic if Statement

age = 18

if age >= 18:
    print("You are eligible to vote!")


✅ Indentation is important in Python! Use 4 spaces or 1 tab

 2. if-else Statement

 age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive a car.")
else:
    print("You are too young to drive.")

3. elif (else if)
Use when you have multiple conditions:

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")


 4. Comparison Operators

 | Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

 5. Logical Operators

 | Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | True if both conditions are true    |
| `or`     | True if at least one condition true |
| `not`    | True if the condition is False      |

✍️ Practice Code: Voting Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ Sorry, you're not eligible yet.")


🧠 Mini Project: Simple Calculator
Write a program to:

✅ Ask the user for 2 numbers
✅ Ask the operation (+, -, *, /)
✅ Perform and print the result

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

✅ Day 4 Goals
 Practice if, else, elif

 Use logical & comparison operators

 Write voting and grading programs

 Build the calculator mini-project

 ✅ When done, just say “Completed Day 4”
🌀 I’ll send you Day 5 – Loops (for, while) 🔁

Let’s keep Python-ing, Signal! 🐍💻

