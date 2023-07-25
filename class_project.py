# ШАГ. Д/з по сроку 27/07/2023
"""
Создать класс "Проект":
- название,
- дата начала,
- дата dead-line,
- список имён программистов, которые над ним работают.
Дата (DateTime) начала должна браться автоматически при создании объекта проекта.
Реализовать метод str(self)
Список программистов на проекте тоже нужно обработать, чтобы он выводился красиво в str.

Создать методы класса:
1. Изменение даты (DateTime) окончания проекта
2. Добавление программиста на проект
3. Метод увольнения программиста с проекта.
"""
from datetime import datetime, timedelta


class Project:
    _name: str
    _start_date: datetime
    _dead_line: datetime
    _programmers: list[str]

    def __init__(self, name: str, start_date: datetime = datetime.now(), dead_line: datetime = None):
        """
        Инициализация проекта
        :param name: Имя проекта
        :param start_date: Дата начала проекта. По умолчанию равна текущим дата/время
        :param dead_line: Планируемая дата окончания проекта.
            По умолчанию (если не определено иное) - Дата начала проекта + 30 дней.
        """
        self._name = name
        self._start_date = start_date
        if dead_line is None or dead_line <= start_date:
            self._dead_line = self._start_date + timedelta(days=30)
        self._programmers = list()

    def __str__(self):
        res = f'Название проекта:\t\t{self._name}\n' \
              f'Дата начала:\t\t\t{self._start_date.strftime("%d.%m.%Y %H:%M:%S")}\n' \
              f'Дата окончания проекта:\t{self._dead_line.strftime("%d.%m.%Y %H:%M:%S")}\n' \
              f'{"-" * 43}\nСписок участников проекта (программистов):\n'
        if bool(self._programmers):
            for index in range(len(self._programmers)):
                res += f'\t{index}. {self._programmers[index]}\n'
        else:
            res += '--- НАД ПРОЕКТОМ НИКТО НЕ РАБОТАЕТ ---'.center(42)
        return res + f'{"-" * 43}\n'

    def add_programmer(self, programmer: str) -> int:
        """
        Добавление программиста в список _programmers
        :param programmer: "Имя Фамилия" добавляемого программиста
        """
        if programmer not in self._programmers:
            self._programmers.append(programmer)
            return len(self._programmers) - 1
        else:
            return -1

    def dismiss_programmer(self, programmer: any([str, int])) -> bool:
        """
        Увольнение программиста. Фактически - удаление из списка _programmers.
        :param programmer: Принимает значение как int (удаление из списка по ID), либо str (удаление из списка по имени)
        """
        try:
            if type(programmer) is int:
                del self._programmers[programmer]
            elif type(programmer) is str:
                self._programmers.remove(programmer)
            else:
                raise ValueError(f'Необрабатываемый передаваемый тип аргумента {type(programmer)}')
        except Exception:  # [IndexError, ValueError]:
            return False
        else:
            return True

    def set_name(self, value: str):
        self._name = value

    def set_start_date(self, value: datetime):
        self._start_date = value

    def set_dead_line(self, value: datetime):
        self._dead_line = value

    name: str = property(fget=lambda self: self._name, fset=set_name, doc='Название проекта')
    start_date: datetime = property(fget=lambda self: self._start_date, fset=set_start_date, doc='Дата/время начала '
                                                                                                 'выполнения проекта')
    dead_line: datetime = property(fget=lambda self: self._dead_line, fset=set_dead_line, doc='Срок выполнения проекта')
    programmers: list[str] = property(fget=lambda self: self._programmers, doc='Список программистов')


if __name__ == '__main__':
    main_project = Project('Главный проект')
    main_project.add_programmer('Aleksandr Situn')  # [0]
    main_project.add_programmer('Заливко Денис')  # [1]
    main_project.add_programmer('Петров Пётр')  # [2]
    main_project.add_programmer('Сидоров Сидор')  # [3]
    main_project.add_programmer('Aleksandr Situn')  # Не добавляется, т.к. уже есть в списке
    print(main_project)
    print("""
        {
            main_project.dead_line = main_project.dead_line + timedelta(days=14)  # Оттянем deadline на 2 недельки )))
            
            main_project.dismiss_programmer(2)  # Увольняем [2] - 'Петров Пётр'
            main_project.dismiss_programmer('Сидоров Сидор')  # Увольняем 'Сидоров Сидор'
            main_project.dismiss_programmer(10)  # Увольняем отсутствующего в списке
            main_project.dismiss_programmer('Unknown Unknown')  # Увольняем отсутствующего в списке
        }
    """)
    main_project.dead_line = main_project.dead_line + timedelta(days=14)  # Оттянем deadline на 2 недельки )))
    main_project.dismiss_programmer(2)  # Увольняем [2] - 'Петров Пётр'
    main_project.dismiss_programmer('Сидоров Сидор')  # Увольняем 'Сидоров Сидор'
    main_project.dismiss_programmer(10)  # Увольняем отсутствующего в списке
    main_project.dismiss_programmer('Unknown Unknown')  # Увольняем отсутствующего в списке
    print(main_project)
