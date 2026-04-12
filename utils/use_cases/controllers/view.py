from typing import Generic


from utils.use_cases.abstract import AbstractUseCase
from utils.use_cases.exceptions import UseCaseExecuteError, UseCaseValidationError
from utils.use_cases.typing import UseCaseActionReturn


class ViewUseCaseController(Generic[UseCaseActionReturn]):
    def __init__(self, use_case: AbstractUseCase[UseCaseActionReturn]):
        self._use_case = use_case

    def execute(self) -> UseCaseActionReturn:
        try:
            result = self._use_case.execute()
        except UseCaseExecuteError as error:
            raise error
        except UseCaseValidationError as errors:
            raise errors

        return result
