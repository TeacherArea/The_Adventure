import flet as ft

from character import create_player
from story import village_intro, shop_intro, clear_screen
from shop import buy_weapon
from scenes.village import village_scene
from scenes.shop import shop_scene
from scenes.wood import wood_scene
from scenes.bridge import bridge_scene
from scenes.ruin import ruin_scene

def main(page: ft.Page):
    player = create_player(name = "Pelle")
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH

    def change_scene(scene):
        page.clean()
        page.title = "The Adventure";

        if(scene == "village"):
            page.add(village_scene(player, change_scene))
        elif(scene == "bridge"):
            page.add(bridge_scene(player, change_scene))
        elif(scene == "shop"):
            page.add(shop_scene(player, change_scene))
        elif(scene == "wood"):
            page.add(wood_scene(player, change_scene))
        elif(scene == "ruin"):
            page.add(ruin_scene(player, change_scene))

        page.update()

    change_scene("village")


if __name__ == "__main__":
    ft.run(main)
