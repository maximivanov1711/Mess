import random


print('Вы запустили программу для генерации mess-ключа, для повторной генерации нажмите Enter...\
      \nНе передавайте этот ключ никому, кроме собеседника')
while True:
    closed_key = random.randint(10000, 1000000000)
    print(closed_key, end='')
    input()

