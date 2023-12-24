# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
list_new = [0, 0, 0, 0, 0]
length = len(list)
K = int(input())
for i in range(length):
    if i >= K: 
        list_new[i - 3] = list[i]
    else:
        list_new[length + (i - K)] = list[i]
print(list_new)