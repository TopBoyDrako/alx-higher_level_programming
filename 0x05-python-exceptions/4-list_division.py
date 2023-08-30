#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float))
            or not isinstance(my_list_2[i], (int, float)):
                result.append(0)
                print("wrong type")
            elif my_list_2[i] == 0:
                result.append(0)
                print("division by 0")
            else:
                division_result = my_list_1[i] / my_list_2[i]
                result.append(division_result)
        except IndexError:
            result.append(0)
            print("out of range")
    return result
        except:
            division_result = 0
            print("wrong type")
        finally:
            result.append(division_result)
    return result
