#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for item in range(list_length):
        try:
            div = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        finally:
            list.append(div)
    return list