from typing import Union, Optional
from flet import *
from flet.border import Border
from flet.control import OptionalNumber
from flet.gradients import Gradient
from flet.types import PaddingValue, MarginValue, BorderRadiusValue

from FletCarousel import FletCarousel


class AutoCycle:
    duration: int

    def __init__(self, duration: int = 1):
        self.duration = duration


class FletCarouselOne(FletCarousel):
    current_items: tuple = 0, 0

    def __init__(
            self,
            page: Page,
            items: Optional[list[Control]] = None,
            items_count: Optional[int] = 1,
            vertical_alignment: CrossAxisAlignment = CrossAxisAlignment.CENTER,
            items_alignment: MainAxisAlignment = MainAxisAlignment.NONE,
            spacing: OptionalNumber = None,
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
            auto_cycle: AutoCycle = None,
            buttons: Optional[list[TextButton | IconButton | FloatingActionButton]] = None,
    ):
        FletCarousel.__init__(
            self,
            page=page,
            width=width,
            height=height,
            expand=expand,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            padding=padding,
            margin=margin,
            alignment=alignment,
            bgcolor=bgcolor,
            gradient=gradient,
            border=border,
            border_radius=border_radius,
        )

        self.items = items
        self.items_count = items_count
        self.vertical_alignment = vertical_alignment
        self.items_alignment = items_alignment
        self.spacing = spacing
        self.auto_cycle = auto_cycle
        self.buttons = buttons

        if len(items) > 0:
            self.current_items = (0, self.items_count)

        self.__update_buttons()

    def build(self) -> Container:

        self.__carousel = Row(
            controls=self.__controls(self.items),
            expand=True,
            alignment=MainAxisAlignment.SPACE_AROUND
        )

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
            content=self.__carousel
        )

    def __controls(self, items: Optional[list[Control]] = None):

        self.__item_list = Row(
            controls=[] if len(items) == 0 else (
                items[0:self.items_count] if len(items) >= self.items_count else items
            ),
            vertical_alignment=self.vertical_alignment,
            spacing=self.spacing,
            alignment=self.items_alignment,
        )

        c = [self.__item_list]

        if not self.buttons or len(self.buttons) == 0:
            return c

        c.insert(0, self.buttons[0])

        if len(self.buttons) >= 2:
            c.append(self.buttons[1])

        return c

    def next(self, e=None):
        if self.__item_list.controls and self.current_items[1] < len(self.items):
            self.current_items = self.current_items[0] + 1, self.current_items[1] + 1
            self.__item_list.controls = self.items[self.current_items[0]:self.current_items[1]]
        self.page.update(self.__item_list)

    def perv(self, e=None):
        if self.__item_list.controls and self.current_items[0] > 0:
            self.current_items = self.current_items[0] - 1, self.current_items[1] - 1
            self.__item_list.controls = self.items[self.current_items[0]:self.current_items[1]]
        self.page.update(self.__item_list)

    def __update_buttons(self):
        if self.buttons or len(self.buttons) > 0:
            self.buttons[0].on_click = self.perv

            if len(self.buttons) >= 2:
                self.buttons[1].on_click = self.next

    def update_items(self, new_items: Optional[list[Control]] = None):
        self.__carousel.controls = self.__controls(new_items)
        self.__carousel.update()

    def reset_items_index(self):
        if self.items:
            # self.update_items(self.items)
            self.current_items = (0, self.items_count)

    def __auto_cycle(self):
        if self.items and self.auto_cycle:
            self.current_items = (0, self.items_count)
            while 1:
                time.sleep(self.auto_cycle.duration)
                self.next()
                if self.current_items[1] == len(self.items):
                    self.current_items = (0, self.items_count)

    def init_state(self):
        self.__auto_cycle()
