"""
This python script takes a number from the user and prints 
the multiplication table for that number from 1 to 10.
"""
number = int(input("Enter a number to see its multiplication table: "))

for x in range(1, 11):
    print(str(number) + " * " + str(x) + " = " + str(number * x ))
