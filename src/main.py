import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)
    page.title = "The Adventure";
    page.bgcolor = ft.Colors.AMBER

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )
    page.add(
        ft.Text("This is the story", ft.Colors.WHITE),
        ft.Text("And this is another story")
    )


if __name__ == "__main__":
    ft.run(main)
