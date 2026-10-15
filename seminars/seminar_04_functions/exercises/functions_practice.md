# Практические задания: Функции

## Подготовка

Для большинства задач есть **заготовка** в папке [`starter/`](starter/): в ней записано
условие и набран каркас кода.

```bash
# запустить заготовку
python seminars/seminar_04_functions/exercises/starter/task_1_1.py
```

Примеры кода к каждой части — в папке [`../examples/`](../examples/).

> **Как работать с заданиями:** прочитайте условие, напишите и **запустите** свою версию,
> и только потом раскройте решение для сверки. Если ваш код работает правильно,
> он тоже верный — решение здесь не единственное.

---

## Часть 1: Первые функции

> **Теория:** [README.md — Блок 1](../README.md#блок-1-функции-def-параметры-return-10-мин) | **Примеры:** [`examples/01_functions_basics.py`](../examples/01_functions_basics.py)

### Задание 1.1

Заготовка: [`starter/task_1_1.py`](starter/task_1_1.py)

Напишите функцию `print_title`, которая принимает текст заголовка и печатает его между
двумя линиями из 30 знаков `=`. Вызовите её для заголовков «Меню», «Заказы» и «Отчёт».

```
==============================
Меню
==============================
```

<details>
<summary>Подсказка</summary>

Определение начинается с `def`, имя параметра указывается в скобках, тело пишется
с отступом. Линию из одинаковых символов даёт повторение строки (семинар 1).

</details>

<details>
<summary>Решение</summary>

```python
def print_title(title):
    """Напечатать заголовок между двумя линиями."""
    print("=" * 30)
    print(title)
    print("=" * 30)


print_title("Меню")
print_title("Заказы")
print_title("Отчёт")
```

Три строки оформления написаны один раз, а используются трижды — это и есть главная
польза функции.

</details>

### Задание 1.2

Заготовка: [`starter/task_1_2.py`](starter/task_1_2.py)

Напишите функцию `trip_cost`, которая принимает расстояние в километрах и цену
за километр и **возвращает** стоимость поездки. Посчитайте стоимость двух поездок:
12 км по 22 рубля и 5 км по 30 рублей. Выведите обе стоимости и общую сумму.

<details>
<summary>Подсказка</summary>

Функция должна не печатать результат, а отдавать его: тогда обе стоимости можно
сохранить в переменные и сложить.

</details>

<details>
<summary>Решение</summary>

```python
def trip_cost(distance, price_per_km):
    """Вернуть стоимость поездки в рублях."""
    return distance * price_per_km


first = trip_cost(12, 22)
second = trip_cost(5, 30)

print("Первая поездка:", first)  # 264
print("Вторая поездка:", second)  # 150
print("Всего:", first + second)  # 414
```

Если бы функция печатала стоимость вместо `return`, сложить результаты было бы нечем:
вызов вернул бы `None`.

</details>

### Задание 1.3

Заготовка: [`starter/task_1_3.py`](starter/task_1_3.py)

Напишите функцию `is_even`, которая возвращает `True` для чётного числа и `False`
для нечётного. Спросите у пользователя число и с помощью этой функции напечатайте
«Чётное» или «Нечётное».

<details>
<summary>Подсказка</summary>

Результат сравнения `number % 2 == 0` — это уже `True` или `False`,
его можно сразу вернуть.

</details>

<details>
<summary>Решение</summary>

```python
def is_even(number):
    """Проверить, является ли число чётным."""
    return number % 2 == 0


number = int(input("Введите число: "))

if is_even(number):
    print("Чётное")
else:
    print("Нечётное")
```

Условие `if is_even(number):` читается как предложение — в этом и смысл хороших
имён функций.

</details>

---

## Часть 2: Аргументы

> **Теория:** [README.md — Блок 2](../README.md#блок-2-аргументы-по-умолчанию-и-именованные-10-мин) | **Примеры:** [`examples/02_arguments.py`](../examples/02_arguments.py)

### Задание 2.1

Заготовка: [`starter/task_2_1.py`](starter/task_2_1.py)

Напишите функцию `format_price`, которая принимает сумму и название валюты и возвращает
строку вида `250 руб.`. Если валюту не передали, подставляется «руб.». Вызовите функцию
тремя способами: только с суммой; с суммой и валютой по порядку; с суммой и валютой,
переданной как именованный аргумент.

```
250 руб.
99 $
1500 €
```

<details>
<summary>Решение</summary>

```python
def format_price(amount, currency="руб."):
    """Вернуть строку с суммой и валютой."""
    return f"{amount} {currency}"


print(format_price(250))
print(format_price(99, "$"))
print(format_price(1500, currency="€"))
```

</details>

### Задание 2.2

Заготовка: [`starter/task_2_2.py`](starter/task_2_2.py)

Напишите функцию `delivery_cost(weight, is_express)`, где второй параметр по умолчанию
означает обычную доставку:

| Вес | Стоимость |
|-----|-----------|
| меньше 1 кг | 200 руб. |
| от 1 до 5 кг | 350 руб. |
| больше 5 кг | 500 руб. |

Экспресс-доставка дороже на 50%, итог округляется до целых рублей.

<details>
<summary>Подсказка</summary>

`return` сразу завершает функцию, поэтому ветки можно писать одну за другой, без `else`.
Но посчитать надбавку нужно **после** того, как базовая цена определена.

</details>

<details>
<summary>Решение</summary>

```python
def delivery_cost(weight, is_express=False):
    """Вернуть стоимость доставки посылки в рублях."""
    if weight < 1:
        price = 200
    elif weight <= 5:
        price = 350
    else:
        price = 500

    if is_express:
        price = round(price * 1.5)

    return price


print(delivery_cost(0.5))  # 200
print(delivery_cost(3))  # 350
print(delivery_cost(7))  # 500
print(delivery_cost(3, True))  # 525
print(delivery_cost(0.5, is_express=True))  # 300
```

Сравните вызовы `delivery_cost(3, True)` и `delivery_cost(3, is_express=True)` —
второй понятнее без заглядывания в определение функции.

</details>

### Задание 2.3

_Задача на разбор кода, заготовки нет._

Дана функция:

```python
def book_ticket(film, seat, price=450):
    print(f"{film}, место {seat}, {price} руб.")
```

Какие из этих вызовов сработают, а какие приведут к ошибке? Для ошибочных объясните
причину.

```python
book_ticket("Матрица", 12)
book_ticket("Интерстеллар", 5, 600)
book_ticket("Довод")
book_ticket(seat=7, film="Начало")
book_ticket("Солярис", price=300)
book_ticket(film="Сталкер", 3)
```

<details>
<summary>Решение</summary>

| Вызов | Результат |
|-------|-----------|
| `book_ticket("Матрица", 12)` | ✅ `Матрица, место 12, 450 руб.` — цена по умолчанию |
| `book_ticket("Интерстеллар", 5, 600)` | ✅ `Интерстеллар, место 5, 600 руб.` |
| `book_ticket("Довод")` | ❌ `TypeError` — не передан обязательный аргумент `seat` |
| `book_ticket(seat=7, film="Начало")` | ✅ именованные аргументы можно переставлять |
| `book_ticket("Солярис", price=300)` | ❌ `TypeError` — `seat` снова не передан |
| `book_ticket(film="Сталкер", 3)` | ❌ `SyntaxError` — позиционный аргумент не может идти после именованного |

</details>

---

## Часть 3: Области видимости и возврат значений

> **Теория:** [README.md — Блок 3](../README.md#блок-3-области-видимости-и-возврат-нескольких-значений-10-мин) | **Примеры:** [`examples/03_scope_and_return.py`](../examples/03_scope_and_return.py)

### Задание 3.1

_Задача на разбор кода, заготовки нет._

Что выведет эта программа? Сначала ответьте сами, потом проверьте.

```python
balance = 1000


def spend(balance, amount):
    balance = balance - amount
    print("внутри:", balance)


spend(balance, 300)
print("снаружи:", balance)
```

<details>
<summary>Решение</summary>

```
внутри: 700
снаружи: 1000
```

Параметр `balance` — локальная переменная функции. Присваивание внутри меняет только её,
а глобальная переменная с тем же именем остаётся прежней. Чтобы сохранить изменение,
значение нужно вернуть из функции: `balance = spend(balance, 300)`.

</details>

### Задание 3.2

Заготовка: [`starter/task_3_2.py`](starter/task_3_2.py)

Напишите функцию `sum_and_average`, которая принимает список чисел и возвращает сразу
два значения — сумму и среднее арифметическое. Результат распакуйте в две переменные
и выведите.

<details>
<summary>Подсказка</summary>

После `return` можно перечислить значения через запятую. Сумму списка даёт встроенная
функция `sum()`, количество элементов — `len()`.

</details>

<details>
<summary>Решение</summary>

```python
def sum_and_average(numbers):
    """Вернуть сумму и среднее арифметическое списка чисел."""
    total = sum(numbers)
    return total, total / len(numbers)


numbers = [12, 7, 30, 3, 25]
total, average = sum_and_average(numbers)

print(f"Сумма: {total}, среднее: {average}")  # Сумма: 77, среднее: 15.4
```

Функция возвращает кортеж — его можно и не распаковывать:
`result = sum_and_average(numbers)`, тогда `result[0]` это сумма.

</details>

### Задание 3.3

Заготовка: [`starter/task_3_3.py`](starter/task_3_3.py)

Программа должна накапливать стоимость заказа, но всегда печатает 0:

```python
total = 0


def add_item(price):
    total = total + price


add_item(180)
add_item(120)

print("Итого:", total)
```

Объясните, почему сумма не растёт, и напишите рабочий вариант. Инструкцией `global`
пользоваться нельзя.

<details>
<summary>Подсказка</summary>

Функция, которая должна что-то изменить, пусть принимает текущее значение
и возвращает новое.

</details>

<details>
<summary>Решение</summary>

Присваивание `total = total + price` создаёт внутри функции **новую локальную**
переменную, а глобальная остаётся нетронутой. Более того, этот код даже не запустится:
Python считает `total` локальной переменной и сообщит, что она используется
до присваивания (`UnboundLocalError`).

```python
def add_item(current, price):
    """Вернуть сумму заказа с добавленным товаром."""
    return current + price


total = 0
total = add_item(total, 180)
total = add_item(total, 120)

print("Итого:", total)  # 300
```

</details>

---

## Для самостоятельной работы

Задачи на темы, которые мы не разбираем на занятии: `*args`, `**kwargs`, лямбда-функции
и функции высшего порядка (теория — в
[README](../README.md#темы-лекции-которые-мы-не-разбираем-на-занятии), примеры —
в файле [`examples/04_args_kwargs_lambda.py`](../examples/04_args_kwargs_lambda.py)).
Сдавать не нужно, решения приложены.

### Задание 4.1

Напишите функцию `average`, которая принимает **любое количество** чисел и возвращает
их среднее арифметическое. Для пустого вызова функция должна возвращать 0.

<details>
<summary>Подсказка</summary>

Звёздочка перед именем параметра собирает все переданные значения в кортеж.

</details>

<details>
<summary>Решение</summary>

```python
def average(*numbers):
    """Вернуть среднее арифметическое переданных чисел."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(average(2, 4, 6))  # 4.0
print(average(5))  # 5.0
print(average())  # 0
```

</details>

### Задание 4.2

Напишите функцию `make_order`, которая принимает название товара и **любые
дополнительные именованные аргументы**, а возвращает словарь с заказом.

```
make_order("Кофе", size="большой", milk="овсяное")
{'product': 'Кофе', 'size': 'большой', 'milk': 'овсяное'}
```

<details>
<summary>Решение</summary>

```python
def make_order(product, **options):
    """Собрать словарь заказа из названия товара и дополнительных опций."""
    order = {"product": product}
    for key, value in options.items():
        order[key] = value
    return order


print(make_order("Кофе"))
print(make_order("Кофе", size="большой", milk="овсяное"))
```

</details>

### Задание 4.3

Дан список городов `["Москва", "Долгопрудный", "Сочи", "Санкт-Петербург"]`.
Решите три задачи:

1. отсортируйте города по длине названия;
2. оставьте только названия длиннее шести букв;
3. получите список длин названий.

Второй и третий пункты решите двумя способами: через `filter()`/`map()`
и через списочное выражение.

<details>
<summary>Решение</summary>

```python
cities = ["Москва", "Долгопрудный", "Сочи", "Санкт-Петербург"]

print(sorted(cities, key=lambda city: len(city)))

# через filter() и map()
print(list(filter(lambda city: len(city) > 6, cities)))
print(list(map(len, cities)))

# через списочные выражения — обычно читается лучше
print([city for city in cities if len(city) > 6])
print([len(city) for city in cities])
```

</details>

### Задание 4.4

Перепишите FizzBuzz с семинара 2 так, чтобы функция `fizzbuzz(number)` **возвращала**
строку, а цикл только печатал результат.

<details>
<summary>Подсказка</summary>

Функция, которая возвращает значение вместо печати, удобнее: её результат можно
вывести, сохранить в список или проверить тестом.

</details>

<details>
<summary>Решение</summary>

```python
def fizzbuzz(number):
    """Вернуть Fizz, Buzz, FizzBuzz или само число строкой."""
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


for number in range(1, 31):
    print(fizzbuzz(number))
```

</details>

### Задание 4.5

Напишите функцию `count_words(text)`, которая принимает предложение и возвращает
словарь «слово — сколько раз встречается».

```
count_words("кот и пёс и кот")
{'кот': 2, 'и': 2, 'пёс': 1}
```

<details>
<summary>Подсказка</summary>

Разбейте текст на слова, заведите пустой словарь и наполняйте его в цикле —
как в задаче про частоту букв с семинара 3.

</details>

<details>
<summary>Решение</summary>

```python
def count_words(text):
    """Посчитать, сколько раз каждое слово встречается в тексте."""
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


print(count_words("кот и пёс и кот"))
```

</details>

### Задание 4.6

Напишите калькулятор на функциях: отдельные функции `add`, `subtract`, `multiply`
и `divide`, каждая возвращает результат. Программа спрашивает два числа и знак
операции, а затем выводит ответ. Деление на ноль должно выдавать понятное сообщение,
а не ошибку.

<details>
<summary>Решение</summary>

```python
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        return "на ноль делить нельзя"
    return first / second


first = float(input("Первое число: "))
operation = input("Операция (+ - * /): ")
second = float(input("Второе число: "))

if operation == "+":
    print(add(first, second))
elif operation == "-":
    print(subtract(first, second))
elif operation == "*":
    print(multiply(first, second))
elif operation == "/":
    print(divide(first, second))
else:
    print("Неизвестная операция")
```

</details>
