import dataclasses

from utils.use_cases import ViewUseCaseController, AbstractUseCase
from utils.use_cases.exceptions import UseCaseExecuteError


@dataclasses.dataclass
class ExampleUseCase(AbstractUseCase):
    a: int
    b: int

    def validate(self):
        if self.a != 1:
            self.errors.add('Число "a" должно ровняться единице!', 'default')

        if self.b != 1:
            raise UseCaseExecuteError('Число "b" должны ровняться единице!')

    def action(self) -> int:
        return self.a + self.b


use_case = ExampleUseCase(a=2, b=1)
print(ViewUseCaseController(use_case).execute())
