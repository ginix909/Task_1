from collections import Counter

encoded_string = list('sos')
latin_alphabet = list('abcdefghijklmnopqrstuvwxyz')

def is_in_latin_alphabet():
    if 2 <= len(encoded_string) <= 1000:
        for x in encoded_string:
            if x in latin_alphabet:
                continue
            else:
                ValueError
                print(f'Symbol {x} is not in Latin Alphabet')
    else:
        print(f'Количество символов в строке {len(encoded_string)}, ожидается от 2 до 1000')

def searching_letter():
    result_list =[]
    result_string = ''
    counter_occurrences = dict(Counter(encoded_string))

    for k, v in counter_occurrences.items():
        if v >= 2:
            result_list.append(k)
    result_string = result_string.join(result_list)
    print(result_string)

searching_letter()
