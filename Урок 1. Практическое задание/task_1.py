"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
name = input("Введите Ваше имя")
passwd = input('Введите Ваш пароль')
age = int(input("Введите Ваш возраст"))
print(f"Ваши данные для входа в аккаунт: имя - {name}, пароль - {passwd}, возраст - {age}")