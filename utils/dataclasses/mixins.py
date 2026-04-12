import dataclasses
import typing
from dataclasses import dataclass
from typing import get_type_hints


@dataclass
class ParseNestedObjectsFromDictMixin:
    """
    Mixin для сборки всех вложенных dataclasses с json/dict.
    """

    @classmethod
    def from_dict(cls, data: dict):
        cls_fields_type_hints: dict = get_type_hints(cls, include_extras=True)

        prepared_data = {}
        for field_name, field_value in data.items():
            field_hint = cls_fields_type_hints[field_name]

            if dataclasses.is_dataclass(field_hint):
                prepared_data[field_name] = field_hint.from_dict(field_value)
                continue

            field_args = typing.get_args(field_hint)
            if field_args and type(field_value) is list and dataclasses.is_dataclass(field_args[0]):
                prepared_data[field_name] = [field_args[0].from_dict(v) for v in field_value]
                continue

            prepared_data[field_name] = field_value

        return cls(**{field: value for field, value in prepared_data.items()})  # noqa
