from copy import deepcopy
from typing import Optional

from utils.use_cases.typing import WarningDTO


class WarningHandler:
    def __init__(self):
        self._warnings: list[WarningDTO] = []

    def exist(self) -> bool:
        return bool(self._warnings)

    def add(
        self,
        message: str,
        object_id: Optional[int] = None,
        object_name: Optional[str] = None,
        extra_object_id: Optional[str] = None,
    ):
        self._warnings.append(
            WarningDTO(
                message=message,
                object_id=object_id,
                object_name=object_name,
                extra_object_id=extra_object_id,
            )
        )

    def extend(self, warnings: list[WarningDTO]):
        self._warnings.extend(warnings)

    def get(self) -> list[WarningDTO]:
        return deepcopy(self._warnings)
