"""Связка двух тем семинара: объект, который сохраняет себя в файл.

Пример для самостоятельного изучения.

Запуск:
    python seminars/seminar_05_files_and_classes/examples/04_class_and_file.py
"""


class TodoList:
    """Список дел, который умеет сохраняться в файл и загружаться из него."""

    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

    def add(self, task):
        """Добавить дело в список."""
        self.tasks.append(task)

    def done(self, task):
        """Удалить выполненное дело."""
        if task in self.tasks:
            self.tasks.remove(task)

    def save(self):
        """Записать все дела в файл, по одному в строке."""
        with open(self.filename, "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load(self):
        """Прочитать дела из файла, заменив текущий список."""
        self.tasks = []
        with open(self.filename, encoding="utf-8") as file:
            for line in file:
                self.tasks.append(line.strip())

    def show(self):
        """Напечатать список дел с нумерацией."""
        if len(self.tasks) == 0:
            print("Список пуст")
            return
        number = 1
        for task in self.tasks:
            print(f"{number}. {task}")
            number += 1


# Создаём список, наполняем и сохраняем на диск
todo = TodoList("tasks_output.txt")
todo.add("прочитать материалы семинара")
todo.add("решить задачи")
todo.add("сдать проект")
todo.done("прочитать материалы семинара")
todo.save()
todo.show()

print()

# Другой объект читает тот же файл — данные пережили «перезапуск»
restored = TodoList("tasks_output.txt")
restored.load()
print("Загружено из файла:")
restored.show()

# Обратите внимание: имя файла — тоже атрибут объекта. Благодаря этому
# можно завести сколько угодно списков дел, каждый со своим файлом.
