from ctypes import alignment
from turtle import bgcolor

import flet as ft

from story import village_intro


def village_scene(player, change_scene):

    def go_to_shop(e):
        change_scene("shop")

    def go_to_bridge(e):
        change_scene("bridge")

    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        image=ft.DecorationImage(
            src="village.png",
            fit=ft.BoxFit.COVER
        ),
        content=ft.Container(
            width=600,
            bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.BLACK),
            border_radius=15,
            padding=30,
            content=ft.Column(
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        village_intro(player["name"]),
                        size=24,
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLACK),
                    ),

                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=16,
                        controls=[
                            ft.Button(
                                "Gå till affären",
                                on_click=go_to_shop
                            ),

                            ft.Button(
                                "Gå mot bron",
                                on_click=go_to_bridge
                            )
                        ]
                    )
                ]
            )
        )
    )