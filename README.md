# Flet simple carousel sliders

This project is a carousel sliders pack with different types for the Flet framework. This project is under development, so in
the future, different types of sliders will be added to the project.

# Installation

````shell
pip install fletcarousel
````
or 
````shell
git clone https://github.com/naderidev/flet-carousel
````

# How to use

There are some types of sliders, so in the following, we will explain each type of them.

### BasicHorizontalCarousel

This type of slider is the basic one. This type is horizontal and there are two buttons to control slides.

![Screenshot of the app](https://raw.githubusercontent.com/naderidev/flet-carousel/master/screenshot1.png "Screenshot")

for example:

````python
BasicHorizontalCarousel(
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
````

### Properties

``page``

the main page

#### Container properties

1. ``width`` : slider width

2. ``height`` :slider height

3. ``expand`` : filling available space

4. ``tooltip`` : tooltip

5. ``disabled`` : disabled

6. ``padding`` : padding

7. ``margin`` : margin

8. ``alignment`` : alignment

9. ``bgcolor`` : background color

10. ``gradient`` : gradient

11. ``border`` : border

12. ``border_radius`` : border_radius

#### Slider properties

1. ``items`` : the items that you want to be in slide show

2. ``items_count`` : the count of controls in each slide

3. ``vertical_alignment`` : items vertical_alignment

4. ``items_alignment`` : items alignment

5. ``spacing`` : spacing between items

6. ``auto_cycle`` : auto cycleing (Auto changing slides)

7. ``buttons`` : the list of Slider's buttons that must be two buttons! the first one is the "previous" button and the second is the "next" button

#### Methods

1. ``next`` : next slide

2. ``prev`` :  previous slide

3. ``update_items`` :  updating items

4. ``reset_items_index`` :  reseting items index
 
check out the file ``examples/flet_carousel_basic.py``


### BasicAnimatedHorizontalCarousel

This type of slider works with AnimatedSwitcher and unlike "BasicHorizontalCarousel" has no next and prev button but has hint lines.

![Screenshot of the app](https://raw.githubusercontent.com/naderidev/flet-carousel/master/screenshot2.png "Screenshot")

for example:

````python
BasicAnimatedHorizontalCarousel(
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
````

### Properties

``page``

the main page

#### Container properties

1. ``width`` : slider width

2. ``height`` :slider height

3. ``expand`` : filling available space

4. ``tooltip`` : tooltip

5. ``disabled`` : disabled

6. ``padding`` : padding

7. ``margin`` : margin

8. ``alignment`` : alignment

9. ``bgcolor`` : background color

10. ``gradient`` : gradient

11. ``border`` : border

12. ``border_radius`` : border_radius

#### Slider properties

1. ``items`` : the items that you want to be in slider

2. ``hint_lines`` : hint lines settings

3. ``animated_switcher`` : The AnimatedSwitcher settings

4. ``auto_cycle`` : auto cycleing (Auto changing slides)

#### Methods

1. ``next`` : next slide

2. ``prev`` :  previous slide

3. ``update_items`` :  updating items

4. ``go`` :  go to a specific slide
 
check out the file ``examples/animated_horizontal_basic.py``

Hope to enjoy :)

# Donating
- [buy me a coffee](https://www.buymeacoffee.com/mohammadrezaN)
