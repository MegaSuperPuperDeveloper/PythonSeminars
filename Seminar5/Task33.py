# Задача №33. Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но
# наоборот все максимальные - на минимальные.

lst1 = [1, 3, 3, 3, 4]
def func_2(lst, lst_new=[], min_n=min(lst1), max_n=max(lst1)):
    if len(lst) == 0:
        return lst_new
    elif lst[0] == max_n:
        lst_new.append(min_n)
    else:
        lst_new.append(lst[0])
    return func_2(lst[1:])

print(func_2(lst1))