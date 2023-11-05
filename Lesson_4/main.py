def input_int(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print('Вы ввели некорректное число! Попробуйте ещё раз.')
        else:
            return result

'''
    Написать программу, которая просит пользователя ввести число. Если
    пользователь вводит некорректное число — сообщить об этом и 
    предложить ввести число ещё раз. Повторять это до тех пор, 
    пока пользователь не введёт корректное число.
'''

a = input_int('Введите a:')
b = input_int('Введите b:')

try:
    c = a / b
    print(a / b)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except TypeError:
    print('Параметры недопустимого типа')
except ModuleNotFoundError:
    print('Подключён неизвестный модуль')
except Exception as error:
    print('Что-то пошло не так')
    print(f'{type(error)}: {error}')
else:
    print('Блок выполнен успешно!')

print('Конец программы')

