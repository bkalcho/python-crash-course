# Author: Bojan G. Kalicanin
# Date: 06-Oct-2016
# Simple calculator which performs addition.

while True:
    try:
        f_num = input("First number? ")
        if f_num == 'q':
            break
        s_num = input("Second number? ")
        if s_num == 'q':
            break
        frst_num = int(f_num)
        second_num = int(s_num)
    except ValueError:
        print("You can not perform addition on two non numeric values.")
    else:
        res = frst_num + second_num
        print("Result is: " + str(res))