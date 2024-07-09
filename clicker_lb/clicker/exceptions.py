from typing import Type


def exception_handler(exc_type: Type["ExceptionBase"]):
    def inner(func):
        async def wrapper(self, *args, **kwargs):
            try:
                return await func(self, *args, **kwargs)
            except Exception as e:
                print(111111111111, e, e.args, 1111111111111111)
                raise exc_type()

        return wrapper

    return inner


class ExceptionBase(Exception):
    """Базовый класс исключений"""

    args = "Неизвестная ошибка"
    exception = None

    def __init__(self, *args, exception: Exception = None):
        if args:
            self.args = args
        if exception:
            self.exception = exception

    def __str__(self):
        return f"Ошибка: {self.args[0]}"


class CourseANotScheduledException(ExceptionBase):
    args = ("Курс 'А' не назначен",)


class CourseBNotScheduledException(ExceptionBase):
    args = ("Курс 'Б' не назначен",)


class CourseOPPNotScheduledException(ExceptionBase):
    args = ("Курс 'ОПП' не назначен",)


class TestNotScheduledException(ExceptionBase):
    args = ("Тест не назначен",)
