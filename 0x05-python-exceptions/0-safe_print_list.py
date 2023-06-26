#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0  # Counter variable
    for j in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            j += 1

        except IndexError:
            break
    print()
    return (j)  # Return number of elem printed
