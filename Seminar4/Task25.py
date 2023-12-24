# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
# постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

entered_text = input("enter text: ").split()
new_str = ""
for symbol in entered_text:
    count = new_str.count(symbol)
    if new_str.count(symbol) == 0:
        new_str += f"{symbol} "
    else:
        new_str += f"{symbol}_{count}"
print(new_str)