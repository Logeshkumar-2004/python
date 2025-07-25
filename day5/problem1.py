#for loop 
#example 1
for i in range (5):
    print("hello \n",i)

#example 2
for i in range(1,11):
    print("\n",i)


#example 3
#3. Loop Control Statements
#| Keyword    | Use                      |
#| ---------- | ------------------------ |
#| `break`    | Exit the loop            |
#| `continue` | Skip current iteration   |
#| `pass`     | Do nothing (placeholder) |


for i in range (1,11):
    if i == 5:
        break
    print("\n",i)

for i in range(1,11):
    if i == 5:
        continue
    print("\n",i)

for i in range( 1,11):
    if i == 5:
        pass
    print("\n",i)

#whild loop 

count = 1
while count <= 5:
    print("\n count is ",count)
    count += 1#count  = count+1