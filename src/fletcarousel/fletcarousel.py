import threading
from typing import Union, Optional
from flet import (
    PaddingValue,
    MarginValue,
    BorderRadiusValue,
    ClipBehavior,
    Border,
    OptionalNumber,
    Control,
    Gradient,
    UserControl,
    Page,
    Alignment,
    Container
)


class FletCarousel(UserControl):
    def __init__(
            self,
            page: Page,
            width: OptionalNumber = None,
            height: OptionalNumber = None,
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

    def _build(self):
        super()._build()
        threading.Thread(target=self.init_state).start()

    def build(self):
        return Container(
            width=self.width,
            height=self.height,
            expand=self.expand,
            tooltip=self.tooltip,
            visible=self.visible,
            disabled=self.disabled,
            padding=self.padding,
            margin=self.margin,
            alignment=self.alignment,
            bgcolor=self.bgcolor,
            gradient=self.gradient,
            border=self.border,
            border_radius=self.border_radius,
            clip_behavior=ClipBehavior.HARD_EDGE,
            content=self.render()
        )

    def render(self) -> Control:
        return Control()

    def init_state(self):
        pass
