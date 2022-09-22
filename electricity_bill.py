# Enter the unit.
a = int(input("Enter the unit : "))
if a<= 0:
    print("You are a electricity saver ⚡🍃")
# Checks if a value is greater than 1 and if it s greater than 100.
elif a >= 1 and a<= 100:
# Your electricity bill is a boolean
    print("Your electricity bill is :" ,a*1.5)
# Checks if a value is greater than 100 and if it s greater than 200.
elif a >= 100 and a<= 200:
# Prints out the electricity bill.
    print("Your electricity bill is :",((a-100)*2.5)+100*2.5)
# Check if a value is greater than 200 or greater than 300.
elif a >= 200 and a<= 300:
# Prints out the electricity bill.
    print("Your electricity bill is :",(((a-200)*4)+100*1.5)+100*4)
# Check if a value is greater than 300 and a > = 350.
elif a >= 300 and a<= 350:
# Prints the electricity bill.
    print("Your electricity bill is :",((((a-300)*5)+100*1.5)+100*2.5)+100*5)
# Check if a value is greater than 350
elif a >= 350:
# Prints the electricity bill.
    print("Your electricity bill is :",((((((a-350)*15)+100*1.5)+100*2.5)+100*4)+50*5))