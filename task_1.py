import re

values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',') #разделили символы запятыми, но сисволы остались в кавычках.
ints = map(int, ints_as_strings)   #перевод строковых обозначений в int

lst=list(ints)
print(lst)
tup=tuple(lst)
print(tup)
lst1 = [1, 2, 3, 4, 5]
print(f'Первый {lst1[0]}, последний {lst1[-1]}')


