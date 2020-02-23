import random


def dialog_interface():
        print('...')
        print('Создан ли ключ? [y / n]', end=' ')
        if input().strip() == 'y':
            while True:
                print('Введите закрытый ключ...')
                try:
                    closed_key = int(input().strip())
                    break
                except ValueError:
                    print('Попробуйте еще раз... ключ должен содержать только цифры')
                    continue
        else:
            closed_key = random.randint(10000, 1000000000)
            print(f'Закрытый ключ создан\nclosed_key: {closed_key}')
            print('Сохранить локально? [y /n]', end=' ')
            if input().strip() == 'y':
                with open('closed_key.txt', 'w') as file:
                    file.write(str(closed_key))
                print('Ключ сохранен')
