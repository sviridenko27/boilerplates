class UseCaseException(Exception):
    pass


class UseCaseExecuteError(UseCaseException):
    pass


class UseCaseValidationError(UseCaseException):
    def __init__(self, errors: dict[str, list]):
        self.errors = errors
