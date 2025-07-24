# 🧠 Python Learning Journey – Day 3

## ✅ What I Learned Today
- How to take user input using `input()`
- Type casting from string to int, float, and bool
- Built real-time interactive programs with user input
- Solved average marks calculator problem

---

## 🔹 input() Function

Gets data from the user. Always returns a string by default.

```python
name = input("Enter your name: ")
print("Hello,", name)


🔹 Type Casting in Python
Used to convert input to another type:

age = int(input("Enter your age: "))       # string → int
height = float(input("Enter your height: "))  # string → float

📌 Example:

num1 = input("Enter a number: ")   # str
num2 = input("Enter another: ")    # str
print(num1 + num2)                 # Output: 23 (if inputs are "2", "3")

# Corrected using int():
result = int(num1) + int(num2)
print("Sum:", result)              # Output: 5


| Function  | Description         |
| --------- | ------------------- |
| `int()`   | Converts to Integer |
| `float()` | Converts to Float   |
| `str()`   | Converts to String  |
| `bool()`  | Converts to Boolean |

✍️ Practice Code

name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("What is your height (in feet)? "))
loves_coding = input("Do you love coding? (yes/no): ")

print("\n--- Profile Summary ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Loves Coding:", loves_coding)

🎯 Practice Problem – Marks Average Calculator
Goal: Ask the user how many subjects, take marks for each, and calculate total & average.

total = 0
subjects = int(input("How many subjects? "))

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    total += mark

average = total / subjects
print("Total Marks =", total)
print("Average Marks =", average)

Day 3 Complete!
🟢 Next Up: Day 4 – Conditional Statements (if/else)

Keep it up, Signal 💻🔥 You're now building interactive Python programs!


