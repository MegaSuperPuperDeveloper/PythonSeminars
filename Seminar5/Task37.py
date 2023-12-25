# Задача №37. Дано натуральное число N и последовательность 
# из N элементов. Требуется вывести эту последовательность в
# обратном порядке. Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

my_str = "3 4"
def func_1(str_obj):
    new_str = ""
    for el in reversed(str_obj):
        new_str += el
    return new_str

print(func_1(my_str))

def func_2(str_obj):
    if len(str_obj) <= 1:
        return str_obj
    print(str_obj[:-1])
    return str_obj[-1] + func_2(str_obj[:-1])

print(func_2(my_str))