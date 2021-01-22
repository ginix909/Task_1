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
        #if i == ''.join(reversed(i)):               
        if i == i[::-1]:                             
            list_of_palindrome.append(i)
    print(f'Ответ Роберта:{len(list_of_palindrome)}')

is_palindrom()


