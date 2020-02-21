import random

'''
Шифрование
'''
closed_key = random.randint(1000000000, 10000000000000000000)
print(closed_key)
alphabit = ['П', 'Р']
text = 'Р'

gg = text
crypto_text = alphabit.index(gg)
open_key = crypto_text * closed_key
print(open_key)

'''
Расшифровка
'''
crypto_text = open_key // closed_key
crypto_text = alphabit[int(crypto_text)]
print(crypto_text)

