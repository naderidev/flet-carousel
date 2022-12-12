from flet import *
from fletcarousel.basic.horizontal import BasicAnimatedHorizontalCarousel, HintLine, AutoCycle


def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.rtl = True
    carousel = BasicAnimatedHorizontalCarousel(
        page=page,
        auto_cycle=AutoCycle(duration=2),
        expand=True,
        padding=50,
        hint_lines=HintLine(
            active_color='red',
            inactive_color='white',
            alignment=MainAxisAlignment.CENTER,
            max_list_size=400
        ),
        items=[
            Container(
                content=Text(value=str(i), size=30),
                height=400,
                expand=True,
                bgcolor='red',
                border_radius=15,
                alignment=alignment.center,
            ) for i in range(10)
        ],
    )
    page.add(carousel)


app(target=main)
