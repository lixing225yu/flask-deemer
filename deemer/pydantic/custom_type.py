from typing import List
from pydantic.utils import update_not_none

__all__ = ['choice']


class Choice:
    values: List

    def __init__(self, values):
        self.values = values

    @classmethod
    def __modify_schema__(cls, field_schema) -> None:
        update_not_none(field_schema, values=cls.values)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: str) -> str:
        if value not in cls.values:
            raise ValueError("值范围不合法")
        return value


def choice(values: List):
    return type("Choice", (Choice,), dict(values=values))
