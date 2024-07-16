import threading
from typing import Union, Optional
from flet import (
    ClipBehavior,
    Border,
    Control,
    UserControl,
    Page,
    Alignment,
    Container
)
from flet_core.gradients import Gradient
from flet_core.types import (
    PaddingValue,
    MarginValue,
    BorderRadiusValue,
)


class FletCarousel(Container):
    def __init__(
            self,
            page: Page,
            width: int = None,
            height: int = None,
            expand: Union[None, bool, int] = None,
            tooltip: Optional[str] = None,
            visible: Optional[bool] = None,
            disabled: Optional[bool] = None,
            padding: PaddingValue = None,
            margin: MarginValue = None,
            alignment: Optional[Alignment] = None,
            bgcolor: Optional[str] = None,
            gradient: Optional[Gradient] = None,
            border: Optional[Border] = None,
            border_radius: BorderRadiusValue = None,
    ):
        super().__init__()
        self.page = page
        self.width = width
        self.height = height
        self.expand = expand
        self.tooltip = tooltip
        self.visible = visible
        self.disabled = disabled
        self.padding = padding
        self.margin = margin
        self.alignment = alignment
        self.bgcolor = bgcolor
        self.gradient = gradient
        self.border = border
        self.border_radius = border_radius
        self.clip_behavior = ClipBehavior.HARD_EDGE,

    def build(self):
        self.content = self.render()
        threading.Thread(target=self.init_state).start()

    def render(self) -> Control:
        return Control()

    def init_state(self):
        pass
