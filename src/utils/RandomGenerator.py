# Imports
from faker import Faker
import random
import string

# Consts
from .consts import EMPTY_STRING

# Exception Handler
from .ExceptionHandler import ExceptionHandler


class RandomGenerator():

    @classmethod
    def generate_name(cls):
        fake = cls.__get_faker(cls)

        return f"{fake.first_name_male()} {fake.last_name()}"

    @classmethod
    def generate_password(cls) -> str:
        try:
            return cls.__get_random_string(cls, 20)
        except Exception as ex:
            ExceptionHandler.log_exception(ex)

    def __get_faker(self) -> Faker:
        return Faker()

    def __get_random_string(self, length: int) -> str:
        try:
            characters = string.ascii_lowercase + string.digits + "()[]{}*#$%&_-"

            return EMPTY_STRING.join(random.choice(characters) for _ in range(length))
        except Exception as ex:
            ExceptionHandler.log_exception(ex)
