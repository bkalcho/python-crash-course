# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Handling ZeroDivisionError exception

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")