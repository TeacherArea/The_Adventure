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
                                village_intro(player["name"]),
                                size=24,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=16,
                                wrap=True,
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
            ]
        )
    )