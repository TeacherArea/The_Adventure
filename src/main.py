import flet as ft


def main(page: ft.Page):

    page.title = "The Adventure"
    page.bgcolor = ft.Colors.AMBER

    page.add(
        ft.Container(
            border=ft.border.all(2, ft.Colors.RED)
            ft.Row(
                controls=[
                    ft.Text("This is the story", color=ft.Colors.WHITE),
                    ft.Text("And this is another story"),
                ],
                spacing=50,
            )
        )
    )


if __name__ == "__main__":
    ft.run(main)
