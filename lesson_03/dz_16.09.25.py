alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_black = 436402
square_azov = 37800
square_total = square_black + square_azov
print(f'Загальна площа Чорного та Азовського морів становить: {square_total} км2')
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
first_second_warehouse = 250449
second_third_warehouse = 222950
total_warehouse = 375291
first_warehouse = total_warehouse - second_third_warehouse
second_warehouse = first_second_warehouse - first_warehouse
third_warehouse = total_warehouse - first_second_warehouse
print(f'На першому складі знаходиться: {first_warehouse} товарів')
print(f'На другому складі знаходиться: {second_warehouse} товарів')
print(f'На третьому складі знаходиться: {third_warehouse} товарів')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

month_payment = 1179
month = 1.5 * 12
price = month_payment * month
print(f'Вартість комп\'ютера становить: {price} грн')
# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'Залишок від ділення становить: {a}')
print(f'Залишок від ділення становить: {b}')
print(f'Залишок від ділення становить: {c}')
print(f'Залишок від ділення становить: {d}')
print(f'Залишок від ділення становить: {e}')
print(f'Залишок від ділення становить: {f}')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
piza_big = 274
piza_small = 218
juice = 35
cake = 350
water = 21

number_piza_big = 4
number_piza_small = 2
number_juice = 4
number_cake = 1
number_water = 3
total_price = (piza_big * number_piza_big) + (piza_small * number_piza_small) + (juice * number_juice) + (cake * number_cake) + (water * number_water)
print(f'Вартість замовлення складає: {total_price} грн.')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photo = 232
one_page = 8
number_page = total_photo / one_page
print(f'Для вклеювання фото знадобиться: {number_page} сторінок альбома')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
tank = 48
fuel_consumption = 9 / 100
total_fuel = total_distance * fuel_consumption
total_tank = (total_fuel / tank) - 1
print(f'Для поїздки знадобиться: {total_fuel} літрів пального.')
print(f'Кількість зупинок для дозаправок складе: {total_tank}')
