from collections import defaultdict


class ErrorHandler:
    def __init__(self):
        self._errors: defaultdict[str, list] = defaultdict(list)

    def exist(self) -> bool:
        return bool(self._errors)

    def add(self, msg: str, field_name: str):
        self._errors[field_name].append(msg)

    def get(self) -> dict[str, list]:
        return dict(self._errors)

    def get_list(self) -> list[str]:
        errors = []
        for error_value in self._errors.values():
            errors.extend(list(error_value))
        return errors
