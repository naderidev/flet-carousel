import time
from typing import Union, Optional
from flet import (
    Border,
    Control,
    Page,
    CrossAxisAlignment,
    MainAxisAlignment,
    TextButton,
    FloatingActionButton,
    IconButton,
    Alignment,
    Row,
    AnimatedSwitcherTransition,
    AnimationCurve,
    AnimatedSwitcher,
    Container,
    Column
)
from flet_core.gradients import Gradient
from flet_core.types import (
    PaddingValue,
    MarginValue,
    BorderRadiusValue,
)
from .fletcarousel import FletCarousel
from .attributes import AutoCycle, HintLine


class BasicHorizontalCarousel(FletCarousel):
    current_items: tuple = 0, 0
    _auto_cycle_status: int = 1  # 1:play 0:pause -1:stop

    def __init__(
            self,
            page: Page,
            items: Optional[list[Control]] = None,
            items_count: Optional[int] = 1,
            vertical_alignment: CrossAxisAlignment = CrossAxisAlignment.CENTER,
            items_alignment: MainAxisAlignment = MainAxisAlignment.NONE,
            spacing: int = None,
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
            auto_cycle: AutoCycle = None,
            buttons: Optional[list[TextButton |
                                   IconButton | FloatingActionButton]] = None,
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

    def render(self) -> Row:

        self.__carousel = Row(
            controls=self.__controls(self.items),
            expand=True,
            alignment=MainAxisAlignment.SPACE_AROUND
        )

        return self.__carousel

    def __controls(self, items: Optional[list[Control]] = None):

        self.__item_list = Row(
            controls=[] if len(items) == 0 else (
                items[0:self.items_count] if len(
                    items) >= self.items_count else items
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
            self.current_items = self.current_items[0] + \
                1, self.current_items[1] + 1
            self.__item_list.controls = self.items[self.current_items[0]:self.current_items[1]]
        self.page.update(self.__item_list)

    def prev(self, e=None):
        if self.__item_list.controls and self.current_items[0] > 0:
            self.current_items = self.current_items[0] - \
                1, self.current_items[1] - 1
            self.__item_list.controls = self.items[self.current_items[0]:self.current_items[1]]
        self.page.update(self.__item_list)

    def pause(self):
        self._auto_cycle_status = 0

    def play(self):
        self._auto_cycle_status = 1

    def stop(self):
        self._auto_cycle_status = -1

    def __update_buttons(self):
        if self.buttons or len(self.buttons) > 0:
            self.buttons[0].on_click = self.perv

            if len(self.buttons) >= 2:
                self.buttons[1].on_click = self.next

    def update_items(self, new_items: Optional[list[Control]] = None):
        self.items = new_items
        if len(new_items) > 0:
            self.current_items = (0, self.items_count)
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
                try:
                    match self._auto_cycle_status:
                        case 1:
                            time.sleep(self.auto_cycle.duration)
                            self.next()
                            if self.current_items[1] == len(self.items):
                                self.current_items = (0, self.items_count)
                        case -1:
                            return
                except:
                    break

    def init_state(self):
        self.__auto_cycle()


class BasicAnimatedHorizontalCarousel(FletCarousel):
    current_item: int = 0

    def __init__(
            self,
            page: Page,
            items: Optional[list[Control]] = None,
            width: int = None,
            height: int = None,
            expand: Union[None, bool, int] = None,
            tooltip: Optional[str] = None,
            visible: Optional[bool] = None,
            disabled: Optional[bool] = None,
            padding: PaddingValue = None,
            margin: MarginValue = None, alignment: Optional[Alignment] = None,
            bgcolor: Optional[str] = None,
            gradient: Optional[Gradient] = None, border: Optional[Border] = None,
            border_radius: BorderRadiusValue = None,
            auto_cycle: AutoCycle = None,
            hint_lines: Optional[HintLine] = False,
            animated_swicher: Optional[AnimatedSwitcher] = AnimatedSwitcher(
                transition=AnimatedSwitcherTransition.SCALE,
                duration=500, reverse_duration=100,
                switch_in_curve=AnimationCurve.BOUNCE_OUT,
                switch_out_curve=AnimationCurve.BOUNCE_IN
            )
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
        self.auto_cycle = auto_cycle
        self.hint_lines = hint_lines
        self.animated_swicher = animated_swicher
        if animated_swicher and self.items:
            self.animated_swicher.content = self.items[0] if items else Container(
            )

    def render(self) -> Control:

        _controls = [self.animated_swicher]

        if self.hint_lines:
            self.__hint_lines_element = Row(
                controls=self.__hint_lines_elements(),
                vertical_alignment=CrossAxisAlignment.CENTER,
                alignment=self.hint_lines.alignment,
                spacing=10
            )
            _controls.append(self.__hint_lines_element)

        return Column(
            _controls,
            spacing=20
        )

    def __hint_lines_elements(self):
        return [
            Container(
                bgcolor=self.hint_lines.active_color if i == 0 else self.hint_lines.inactive_color,
                border_radius=20,
                width=int(self.hint_lines.max_list_size /
                          len(self.items)),
                height=5,
                on_click=lambda e, i=i: self.go(i)
            ) for i in range(len(self.items))
        ]

    def next(self, e=None):
        if self.current_item < len(self.items):
            self.go(self.current_item + 1)

    def prev(self, e=None):
        if self.current_item > 0:
            self.go(self.current_item - 1)

    def go(self, index: int):
        if index in range(len(self.items)):
            try:
                self.current_item = index
                self.animated_swicher.content = self.items[self.current_item]
                self.animated_swicher.update()

                if self.hint_lines:

                    for c in self.__hint_lines_element.controls:
                        c.bgcolor = self.hint_lines.inactive_color

                    self.__hint_lines_element.controls[self.current_item].bgcolor = self.hint_lines.active_color
                    self.__hint_lines_element.update()
            except:
                pass

    def __auto_cycle(self):
        if self.items and self.auto_cycle:
            self.current_item = 0
            while 1:
                try:
                    time.sleep(self.auto_cycle.duration)
                    self.next()
                    if int(self.current_item + 1) == len(self.items):
                        time.sleep(self.auto_cycle.duration)
                        self.go(0)
                except:
                    break

    def update_items(self, new_items: Optional[list[Control]] = None):
        self.items = new_items
        self.go(0)
        if self.hint_lines:
            self.__hint_lines_element.controls = self.__hint_lines_elements()
            self.__hint_lines_element.update()

    def init_state(self):
        self.__auto_cycle()
