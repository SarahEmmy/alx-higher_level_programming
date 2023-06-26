#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    for j in range(list_length):
        try:
            div = my_list_1[j] / my_list_2[j]
        except (ValueError, TypeError):
            print("wrong type")
            div = 0
        except (ZeroDivisionError):
            print("division by 0")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0
        finally:
            new_l.append(div)
    return (new_l)
