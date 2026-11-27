from ctypes import alignment
from importlib.resources import contents
from turtle import bgcolor

import flet as ft

from story import shop_intro
from shop import buy_weapon

def shop_scene(player, change_scene):

    def go_to_village():
        change_scene("village")

    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        image=ft.DecorationImage(
            src="shop.png",
            fit=ft.BoxFit.COVER
        ),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    col={"xs": 10, "sm": 10, "md": 8, "lg": 6},
                    bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.BLACK),
                    border_radius=15,
                    padding=30,
                    
                    content=ft.Column(
                        tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                shop_intro(),
                                size=24,
                                color=ft.Colors.WHITE
                            ),

                            ft.ResponsiveRow(
                                alignment=ft.MainAxisAlignment.CENTER,
                                columns=2,
                                spacing=16,
                                run_spacing=16,
                                controls=[
                                    ft.Button(
                                        "Köp träsvärd",
                                        col={"xs": 2, "sm": 1},
                                        on_click=buy_weapon(player, "Träsvärd")
                                    ),
                                    ft.Button(
                                        "Köp järnsvärd",
                                        col={"xs": 2, "sm": 1},
                                        on_click=buy_weapon(player, "Järnsvärd")
                                    ),
                                    ft.Button(
                                            "Lämna shoppen",
                                            col={"xs": 2, "sm": 1},
                                            on_click=go_to_village
                                        ),
                                    ft.Button(
                                        "Lämna shoppen",
                                        col={"xs": 2, "sm": 1},
                                        on_click=go_to_village
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )
