from collections import Counter

input_string = str(input())

def is_in_latin_alphabet():
    latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if 2 <= len(input_string) <= 1000:
        for x in input_string:
            if x in latin_alphabet:
                continue
            else:
                raise ValueError(f'Symbol {x} is not in Latin Alphabet')
    else:
        print(f'Количество символов в строке {len(input_string)}, ожидается от 2 до 1000')

def searching_letter():
    is_in_latin_alphabet()
    result_list =[]
    result_string = ''
    counter_occurrences = dict(Counter(input_string))
    for k, v in counter_occurrences.items():
        if v >= 2:
            result_list.append(k)
            result_string = ''.join(result_list)

    if result_string == '':
        print('В введенной строке нет объектов, встречающихся 2 или более раз')
    else:
        print(result_string)

searching_letter()
