#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    new_result = 0
    for i in range(0, list_length):
        try:
            new_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            new_result = 0
            print("wrong type")
        except ZeroDivisionError:
            new_result = 0
            print("division by 0")
        except IndexError:
            new_result = 0
            print("out of range")
        finally:
            pass
        div.append(new_result)
    return div
