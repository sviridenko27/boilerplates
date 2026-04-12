from typing import TypeVar, Optional
import dataclasses

UseCaseActionReturn = TypeVar('UseCaseActionReturn')


@dataclasses.dataclass
class WarningDTO:
    message: str
    object_id: Optional[int] = None
    object_name: Optional[str] = None
    extra_object_id: Optional[str] = None

