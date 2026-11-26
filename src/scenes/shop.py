import flet as ft

from story import shop_intro
from shop import buy_weapon

def shop_scene(player, change_scene):

    def go_to_village():
        change_scene("village")

    return ft.Container(
        expand=True,

        image=ft.DecorationImage(
            src="shop.png",
            fit=ft.BoxFit.COVER
        ),

        content=ft.Column(
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    shop_intro(),
                    size=24,
                    color=ft.Colors.WHITE
                ),
                ft.Button(
                    "Köp träsvärd",
                    on_click=buy_weapon(player, "Träsvärd")
                ),
                ft.Button(
                    "Köp järnsvärd",
                    on_click=buy_weapon(player, "Järnsvärd")
                ),
                ft.Button(
                    "Lämna shoppen",
                    on_click=go_to_village
                )
            ]
        )
    )
