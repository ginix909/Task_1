# куратор называет любое натуральное число X
# роберт должен ответить сколько существует чисел палиндромов <=X. Также 1 <= X <= 100000

# Логика примерно будет таковой:
# Ввод натурального числа, (пока без исключений) от 1 до 100000

# Алгоритм поиска палиндромов. сначала нужно сгенерировать последовательность чисел меньше Х. потом отфильтровать
# по условию: переводим число в строку, если перевернутая строка равна нашей, то это палиндром.

# поместить их в список и посчитать длину.

curator_number = int(input('Введите натуральное число от 1 до 100000 включительно:'))

def checking_input():
    while True:
        try:
            if 1 <= curator_number <= 100000:
                break
            else:
                print(f'Ваше число {curator_number} находится за границами допустимого предела (от 1 до 100000)')
        except:
            ValueError

def is_palindrom ():
    checking_input()
    less_x_numbers = []

    for i in range(1, curator_number + 1):
        less_x_numbers.append(i)

    list_of_strings = list(map(str, less_x_numbers))
    list_of_palindrome = []
    for i in list_of_strings:
        #if i == ''.join(reversed(i)):               # join создает вид новой строки и reversed ее переворачивате. str immutable, нельзя просто перевернуть. объект str не содержит встроенный метод reverse,
        if i == i[::-1]:                             #обратный срез. самая быстрая практика для палиндрома.
            list_of_palindrome.append(i)
    print(f'Ответ Роберта:{len(list_of_palindrome)}')

is_palindrom()


