#!/usr/bin/python3
# a script to divide twio liosts to a given length

def list_division(my_list_1, my_list_2, list_length):
    reslist = []
    for i in range(0, list_length):
        try:
            elem = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print('wrong type')
            elem = 0
        except (ZeroDivisionError):
            print('division by 0')
            elem = 0
        except (IndexError):
            print('out of range')
            elem = 0
        except (ArithmeticError):
            elem = 0
        finally:
            if (elem is not None):
                reslist.append(elem)
            else:
                continue
    return (reslist)
