from flet import *


def main(page: Page):
    page.title = 'App'

    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    c = Container(
        width=900,
        height=200,
        bgcolor='red',
        border_radius=30,
        animate_position=500,
        animate_opacity=300,
        margin=50,
    )
    carousel = Container(
        content=Stack(
            controls=[
                c
            ],
        ),
        height=300,
        bgcolor='blue',
    )

    page.add(carousel)

    time.sleep(3)

    c.top = -350
    time.sleep(0.1)
    c.opacity = 0
    c.update()

    # for el in carousel.content.controls:
    #     c = 0
    #     while 1:
    #         c += math.pi / 1000
    #         el.top = math.sin(c) * 200
    #         el.update()

    #         if c >= (math.pi / 2):
    #             break
    print('Finish')


app(target=main)
