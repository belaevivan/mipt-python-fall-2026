# Практические задания: Работа с файлами. Классы и объекты

## Подготовка

Данные для заданий лежат в папке [`../data/`](../data/), заготовки — в [`starter/`](starter/).
В заданиях используются **относительные пути**, поэтому запускайте их из папки семинара:

```bash
cd seminars/seminar_05_files_and_classes
python exercises/starter/task_1_1.py
```

Если видите `FileNotFoundError` — проверьте, из какой папки запущена программа.

Примеры кода к каждой части — в папке [`../examples/`](../examples/).

> **Как работать с заданиями:** прочитайте условие, напишите и **запустите** свою версию,
> и только потом раскройте решение для сверки. Если ваш код работает правильно,
> он тоже верный — решение здесь не единственное.

---

## Часть 1: Работа с файлами

> **Теория:** [README.md — Блок 1](../README.md#блок-1-работа-с-файлами-10-мин) | **Примеры:** [`examples/01_files.py`](../examples/01_files.py)

### Задание 1.1

Заготовка: [`starter/task_1_1.py`](starter/task_1_1.py)

В файле [`data/temperatures.txt`](../data/temperatures.txt) записаны измерения
температуры, по одному в строке. Выведите количество измерений и среднюю температуру.

```
Измерений: 7
Средняя температура: 8.34
```

<details>
<summary>Подсказка</summary>

Из файла строки приходят с переносом в конце и как текст — их нужно очистить
и превратить в числа. Накапливайте сумму и количество, как в задачах семинара 2.

</details>

<details>
<summary>Решение</summary>

```python
total = 0
count = 0

with open("data/temperatures.txt", encoding="utf-8") as file:
    for line in file:
        total += float(line.strip())
        count += 1

print("Измерений:", count)
print("Средняя температура:", round(total / count, 2))
```

Здесь нужен именно `float()`: температуры дробные.

</details>

### Задание 1.2

Заготовка: [`starter/task_1_2.py`](starter/task_1_2.py)

В файле [`data/students.txt`](../data/students.txt) каждая строка — «имя;группа;балл».
Выведите каждого студента в виде `Анна (Б01-123): 92`, а в конце — сколько студентов
набрали 80 баллов и больше.

<details>
<summary>Подсказка</summary>

Строку с разделителями разбирают методом `split(";")` — результат сразу распаковывается
в три переменные.

</details>

<details>
<summary>Решение</summary>

```python
excellent = 0

with open("data/students.txt", encoding="utf-8") as file:
    for line in file:
        name, group, score = line.strip().split(";")
        print(f"{name} ({group}): {score}")
        if int(score) >= 80:
            excellent += 1

print("Отличников:", excellent)  # 2
```

Обратите внимание: `score` из файла — строка, поэтому для сравнения нужен `int()`.

</details>

### Задание 1.3

Заготовка: [`starter/task_1_3.py`](starter/task_1_3.py)

Прочитайте `data/students.txt` и запишите в новый файл `report.txt` студентов
с баллом не меньше 80 — по одному в строке, в виде `Анна;92`. Первой строкой
отчёта сделайте заголовок «Отличники». Затем прочитайте `report.txt`
и выведите его содержимое.

<details>
<summary>Подсказка</summary>

`write()` не добавляет перенос строки — его нужно писать самим. Удобно сначала
собрать подходящие строки в список, а потом записать их одним циклом.

</details>

<details>
<summary>Решение</summary>

```python
best = []

with open("data/students.txt", encoding="utf-8") as file:
    for line in file:
        name, group, score = line.strip().split(";")
        if int(score) >= 80:
            best.append(f"{name};{score}")

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Отличники\n")
    for row in best:
        file.write(row + "\n")

with open("report.txt", encoding="utf-8") as file:
    print(file.read())
```

Режим `"w"` каждый раз создаёт файл заново — при повторном запуске старый отчёт
не останется. Если нужно дописывать, используют `"a"`.

</details>

---

## Часть 2: Классы и объекты

> **Теория:** [README.md — Блок 2](../README.md#блок-2-классы-и-объекты-10-мин) | **Примеры:** [`examples/02_classes.py`](../examples/02_classes.py)

### Задание 2.1

Заготовка: [`starter/task_2_1.py`](starter/task_2_1.py)

Опишите класс `Student` с конструктором, который принимает имя, группу и балл.
Создайте двух студентов и выведите их данные в виде `Анна (Б01-123): 92`.

<details>
<summary>Подсказка</summary>

Конструктор — это метод `__init__`, у которого первым параметром идёт `self`.
Внутри данные сохраняют в атрибуты: `self.имя = параметр`.

</details>

<details>
<summary>Решение</summary>

```python
class Student:
    """Студент курса."""

    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score


first = Student("Анна", "Б01-123", 92)
second = Student("Пётр", "Б01-124", 65)

print(f"{first.name} ({first.group}): {first.score}")
print(f"{second.name} ({second.group}): {second.score}")
```

</details>

### Задание 2.2

Заготовка: [`starter/task_2_2.py`](starter/task_2_2.py)

Создайте список из трёх студентов, выведите их всех в цикле и посчитайте средний балл
по списку.

<details>
<summary>Подсказка</summary>

Объекты — обычные значения: список с ними перебирается тем же `for`, что и список
чисел. Внутри цикла доступны все атрибуты объекта.

</details>

<details>
<summary>Решение</summary>

```python
class Student:
    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score


students = [
    Student("Анна", "Б01-123", 92),
    Student("Иван", "Б01-123", 78),
    Student("Пётр", "Б01-124", 65),
]

total = 0
for student in students:
    print(f"{student.name} ({student.group}): {student.score}")
    total += student.score

print("Средний балл:", round(total / len(students), 2))  # 78.33
```

</details>

### Задание 2.3

Заготовка: [`starter/task_2_3.py`](starter/task_2_3.py)

Прочитайте `data/students.txt` и превратите каждую строку в объект `Student`,
сложив их в список. Затем выведите только студентов группы Б01-123.

<details>
<summary>Подсказка</summary>

Это задание 1.2 плюс класс: вместо печати строки создавайте объект и добавляйте
его в список. Балл из файла приходит строкой — преобразуйте его сразу
при создании объекта.

</details>

<details>
<summary>Решение</summary>

```python
class Student:
    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score


students = []

with open("data/students.txt", encoding="utf-8") as file:
    for line in file:
        name, group, score = line.strip().split(";")
        students.append(Student(name, group, int(score)))

for student in students:
    if student.group == "Б01-123":
        print(f"{student.name} ({student.group}): {student.score}")
```

Теперь данные из файла живут в программе как объекты: с ними удобно работать
дальше — фильтровать, сортировать, считать статистику.

</details>

---

## Часть 3: Методы и состояние объекта

> **Теория:** [README.md — Блок 3](../README.md#блок-3-методы-и-состояние-объекта-10-мин) | **Примеры:** [`examples/03_methods.py`](../examples/03_methods.py)

### Задание 3.1

Заготовка: [`starter/task_3_1.py`](starter/task_3_1.py)

Добавьте в класс `Student` два метода: `is_excellent()` возвращает `True`, если балл
не меньше 85, а `describe()` возвращает строку вида `Анна (Б01-123): 92`.
Проверьте оба метода на двух студентах с разными баллами.

<details>
<summary>Подсказка</summary>

Метод отличается от функции только тем, что описан внутри класса и получает `self`
первым параметром. Через `self` он добирается до атрибутов объекта.

</details>

<details>
<summary>Решение</summary>

```python
class Student:
    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score

    def is_excellent(self):
        """Проверить, отличник ли студент."""
        return self.score >= 85

    def describe(self):
        """Вернуть описание студента строкой."""
        return f"{self.name} ({self.group}): {self.score}"


first = Student("Анна", "Б01-123", 92)
second = Student("Пётр", "Б01-124", 65)

print(first.describe(), "— отличник:", first.is_excellent())  # True
print(second.describe(), "— отличник:", second.is_excellent())  # False
```

Метод `describe()` возвращает строку, а не печатает её, — такой результат можно
и вывести, и записать в файл.

</details>

### Задание 3.2

Заготовка: [`starter/task_3_2.py`](starter/task_3_2.py)

Опишите класс `WeatherStation`, который хранит измерения температуры:

| Метод | Что делает |
|-------|------------|
| `add(value)` | добавить измерение |
| `count()` | сколько измерений сделано |
| `average()` | средняя температура (0, если измерений нет) |
| `maximum()` | самое высокое измерение |

<details>
<summary>Подсказка</summary>

Список измерений создавайте в конструкторе — тогда у каждой станции он будет свой.
Метод `add` меняет состояние объекта, остальные три только читают его.

</details>

<details>
<summary>Решение</summary>

```python
class WeatherStation:
    """Метеостанция, которая накапливает измерения температуры."""

    def __init__(self):
        self.measurements = []

    def add(self, value):
        """Добавить измерение."""
        self.measurements.append(value)

    def count(self):
        """Вернуть количество измерений."""
        return len(self.measurements)

    def average(self):
        """Вернуть среднюю температуру."""
        if len(self.measurements) == 0:
            return 0
        return sum(self.measurements) / len(self.measurements)

    def maximum(self):
        """Вернуть самое высокое измерение."""
        return max(self.measurements)


station = WeatherStation()
station.add(12.5)
station.add(8.0)
station.add(19.8)

print("Измерений:", station.count())  # 3
print("Средняя:", round(station.average(), 2))  # 13.43
print("Максимум:", station.maximum())  # 19.8
```

Проверка на пустой список в `average()` нужна, чтобы не делить на ноль.

</details>

### Задание 3.3

Заготовка: [`starter/task_3_3.py`](starter/task_3_3.py)

Опишите класс `StudentCard`, который хранит баллы так, чтобы они всегда оставались
в диапазоне от 0 до 100: `add_points(points)`, `remove_points(points)` и `score()`.
Если операция выводит балл за границы, объект сообщает об этом и оставляет прежнее
значение.

<details>
<summary>Подсказка</summary>

Храните баллы в атрибуте с подчёркиванием в начале имени — это знак, что снаружи
его менять не следует. Проверку делайте **до** изменения атрибута.

</details>

<details>
<summary>Решение</summary>

```python
class StudentCard:
    """Карточка студента с баллами от 0 до 100."""

    def __init__(self, name):
        self.name = name
        self._score = 0

    def add_points(self, points):
        """Добавить баллы, если итог не превысит 100."""
        if self._score + points > 100:
            print("Больше 100 баллов быть не может")
            return
        self._score += points

    def remove_points(self, points):
        """Снять баллы, если итог не станет отрицательным."""
        if self._score - points < 0:
            print("Балл не может быть отрицательным")
            return
        self._score -= points

    def score(self):
        """Вернуть текущий балл."""
        return self._score


card = StudentCard("Анна")
card.add_points(50)
card.add_points(70)  # Больше 100 баллов быть не может
card.remove_points(20)

print(card.score())  # 30
```

Это и есть инкапсуляция: правило «балл от 0 до 100» записано внутри класса,
и обойти его снаружи случайно не получится.

</details>

---

## Для самостоятельной работы

Задачи на связку двух тем семинара и на то, что мы разбирали кратко. Сдавать не нужно,
решения приложены.

### Задание 4.1

Опишите класс `Journal`, который ведёт дневник в файле:

- конструктор принимает имя файла;
- метод `write_entry(text)` **дописывает** строку в конец файла;
- метод `read_all()` возвращает список всех записей.

Проверьте: сделайте три записи, затем прочитайте их и выведите с нумерацией.

<details>
<summary>Подсказка</summary>

Имя файла сохраните атрибутом в конструкторе — тогда методы смогут брать его
из `self`. Для дозаписи нужен режим `"a"`.

</details>

<details>
<summary>Решение</summary>

```python
class Journal:
    """Дневник, который хранит записи в файле."""

    def __init__(self, filename):
        self.filename = filename

    def write_entry(self, text):
        """Дописать запись в конец файла."""
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")

    def read_all(self):
        """Вернуть список всех записей."""
        entries = []
        with open(self.filename, encoding="utf-8") as file:
            for line in file:
                entries.append(line.strip())
        return entries


journal = Journal("journal_output.txt")
journal.write_entry("начал курс по Python")
journal.write_entry("разобрался с файлами")
journal.write_entry("написал первый класс")

number = 1
for entry in journal.read_all():
    print(f"{number}. {entry}")
    number += 1
```

</details>

### Задание 4.2

Перед вами процедурный код управления лампой — похожий разбирали на лекции.
Перепишите его в класс `SmartLamp` с методами `turn_on()`, `turn_off()`,
`set_brightness(value)` и `status()`.

```python
lamp = {"name": "кухня", "is_on": False, "brightness": 0}


def turn_on(device):
    device["is_on"] = True


def set_brightness(device, value):
    device["brightness"] = value
```

<details>
<summary>Подсказка</summary>

Ключи словаря становятся атрибутами, функции — методами, а первый параметр `device`
заменяется на `self`.

</details>

<details>
<summary>Решение</summary>

```python
class SmartLamp:
    """Умная лампа."""

    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        """Включить лампу."""
        self.is_on = True

    def turn_off(self):
        """Выключить лампу и сбросить яркость."""
        self.is_on = False
        self.brightness = 0

    def set_brightness(self, value):
        """Установить яркость от 0 до 100."""
        if value < 0 or value > 100:
            print("Яркость должна быть от 0 до 100")
            return
        self.brightness = value
        self.is_on = value > 0

    def status(self):
        """Вернуть описание состояния лампы."""
        if not self.is_on:
            return f"{self.name}: выключена"
        return f"{self.name}: включена, яркость {self.brightness}"


lamp = SmartLamp("кухня")
lamp.turn_on()
lamp.set_brightness(70)
print(lamp.status())  # кухня: включена, яркость 70

lamp.turn_off()
print(lamp.status())  # кухня: выключена
```

Главная разница: данные лампы и действия над ней теперь лежат в одном месте,
и функции не нужно каждый раз передавать словарь.

</details>

### Задание 4.3

Прочитайте [`data/cities.txt`](../data/cities.txt) и выведите: количество городов,
самое длинное название и список названий длиннее восьми букв.

<details>
<summary>Решение</summary>

```python
cities = []

with open("data/cities.txt", encoding="utf-8") as file:
    for line in file:
        cities.append(line.strip())

print("Городов:", len(cities))
print("Самое длинное название:", max(cities, key=len))
print("Длиннее восьми букв:", [city for city in cities if len(city) > 8])
```

`max()` с параметром `key=len` сравнивает элементы по длине, а не по алфавиту.

</details>

### Задание 4.4

Загрузите студентов из `data/students.txt` в список объектов `Student` (как в задании
2.3) и выведите трёх лучших по баллу.

<details>
<summary>Подсказка</summary>

Отсортировать список объектов по атрибуту поможет `sorted()` с `key=lambda ...`
(семинар 4), а срез `[:3]` оставит первые три элемента.

</details>

<details>
<summary>Решение</summary>

```python
class Student:
    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score


students = []

with open("data/students.txt", encoding="utf-8") as file:
    for line in file:
        name, group, score = line.strip().split(";")
        students.append(Student(name, group, int(score)))

best = sorted(students, key=lambda student: student.score, reverse=True)

for student in best[:3]:
    print(f"{student.name}: {student.score}")
```

`reverse=True` сортирует по убыванию — от большего балла к меньшему.

</details>

### Задание 4.5

Опишите класс `Temperature`, который хранит температуру в градусах Цельсия
в атрибуте `_celsius` и предоставляет методы `celsius()`, `fahrenheit()`
и `set_celsius(value)`. Температура ниже абсолютного нуля (−273.15 °C)
приниматься не должна.

<details>
<summary>Решение</summary>

```python
class Temperature:
    """Температура с проверкой физического минимума."""

    ABSOLUTE_ZERO = -273.15

    def __init__(self, celsius=0):
        self._celsius = 0
        self.set_celsius(celsius)

    def set_celsius(self, value):
        """Установить температуру в градусах Цельсия."""
        if value < self.ABSOLUTE_ZERO:
            print("Температура ниже абсолютного нуля невозможна")
            return
        self._celsius = value

    def celsius(self):
        """Вернуть температуру в градусах Цельсия."""
        return self._celsius

    def fahrenheit(self):
        """Вернуть температуру в градусах Фаренгейта."""
        return self._celsius * 9 / 5 + 32


temperature = Temperature(36.6)
print(temperature.celsius())  # 36.6
print(round(temperature.fahrenheit(), 2))  # 97.88

temperature.set_celsius(-300)  # Температура ниже абсолютного нуля невозможна
print(temperature.celsius())  # 36.6 — значение не изменилось
```

`ABSOLUTE_ZERO` записан в самом классе: это константа, одинаковая для всех объектов.

</details>
