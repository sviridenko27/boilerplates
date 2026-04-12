from abc import ABCMeta, abstractmethod
from typing import Generic

from utils.use_cases.exceptions import UseCaseValidationError
from utils.use_cases.handlers import ErrorHandler, WarningHandler
from utils.use_cases.typing import UseCaseActionReturn


class AbstractUseCase(Generic[UseCaseActionReturn], metaclass=ABCMeta):
    def __post_init__(self):
        self.errors: ErrorHandler = ErrorHandler()
        self.warnings: WarningHandler = WarningHandler()

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def action(self):
        pass

    def execute(self) -> UseCaseActionReturn:
        self.validate()
        self.check_errors()
        return self.action()

    def check_errors(self):
        if self.errors.exist():
            raise UseCaseValidationError(self.errors.get())
