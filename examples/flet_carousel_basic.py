from flet import *

from fletcarousel.horizontal import BasicHorizontalCarousel


def main(page: Page):
    page.theme_mode = ThemeMode.DARK
    page.rtl = True
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    carousel = BasicHorizontalCarousel(
        page=page,
        items_count=3,
        # auto_cycle=AutoCycle(duration=1),
        items=[
            Container(
                content=Text(value=str(i), size=20),
                height=200,
                width=300,
                bgcolor='red',
                border_radius=15,
                alignment=alignment.center,
            ) for i in range(10)
        ],
        buttons=[
            FloatingActionButton(
                icon=icons.NAVIGATE_BEFORE,
                bgcolor='#1f2127'
            ),
            FloatingActionButton(
                icon=icons.NAVIGATE_NEXT,
                bgcolor='#1f2127'
            )
        ],
        vertical_alignment=CrossAxisAlignment.CENTER,
        items_alignment=MainAxisAlignment.CENTER
    )
    page.add(carousel)


app(target=main)
