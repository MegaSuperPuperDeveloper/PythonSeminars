# Задача №35. # Напишите функцию, которая 
# принимает одно число и проверяет, 
# является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def func_1(n):
    count = 1
    count1 = 0
    while count <= n:
        if n % count == 0:
            count1 += 1
        count += 1
    if count1 == 2:
        return "yes"
    return "no"
  
print(func_1(7))


def func_2(n, count = 1, count1 = 0):
    if n % count == 0:
        count1 += 1
    count += 1
    if count > n:
        if count1 == 2:
            return "yes"
        return "no"
    return func_2(n, count, count1)

print(func_2(7))