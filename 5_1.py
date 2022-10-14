# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "Кабвак жабве написать программу, убирабвающую из текста 'абв'?"

text_list = text.split()

new_text = ' '.join([i for i in text_list if 'абв' not in i])

print(text)
print('=> ', new_text)