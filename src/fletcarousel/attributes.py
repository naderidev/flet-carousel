from flet import MainAxisAlignment
from typing import Optional
from pydantic import BaseModel

class AutoCycle:
    duration: int

    def __init__(self, duration: int = 1):
        self.duration = duration


class HintLine(BaseModel):
    active_color: Optional[str]
    inactive_color: Optional[str]
    alignment: Optional[MainAxisAlignment]
    max_list_size: Optional[int]
