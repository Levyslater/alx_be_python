"""
This script will prompt the user to enter a positive integer, 
then use nested loops to print a square pattern of that size made of asterisks (*).
"""
size = int(input("Enter the size of the pattern: "))
count = 0

while count < size:
    for x in range(size):
        print("*", end="")
    print()
    count += 1