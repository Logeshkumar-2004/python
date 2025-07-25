num = int(input("enter a number \n"))
total = 0
while num > 0:
    digits = num % 10
    total += digits #total  = total + digits
    num //= 10 #num = num//10    
    #// means show that number how many times divided 15//10 =1

print("sum of digits=",total)
 