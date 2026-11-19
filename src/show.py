# Tillfällig konsolversion.
# Kör den här filen när du testar ditt spel, inte main.py där flet ska ligga.
# Ett tips är att du gör färdigt ditt program och att använda denna fil för att testa under tiden.
# Byt sen till Flet för att koncentrera dig på att göra ditt program mer tjustigt.

from character import create_player
from story import village_intro, shop_intro, clear_screen
from shop import buy_weapon

import time

name = input("Vad heter din hjälte? ")
player = create_player(name)
current_scene = "village" #behåll denna strukur med "scener", så är det lättare att byta i Flet

while current_scene != "quit":
    if current_scene == "village":
        print("\n" + village_intro(player["name"]))
        print("1. Gå till affären")
        print("2. Gå mot bron")
        print("0. Avsluta")
        choice = input("Ditt val: ")

        if choice == "1":
            current_scene = "shop"
        elif choice == "2":
            current_scene = "bridge"
        elif choice == "0":
            current_scene = "quit"
        else:
            print("Välj ett av alternativen.")

    elif current_scene == "shop":
        print("\n" + shop_intro())
        print(f"Du har {player['gold']} guld och {player['experience']} erfarenhet.")
        print("1. Köp träsvärd (5 guld, 0 erfarenhet)")
        print("2. Köp järnsvärd (15 guld, 10 erfarenhet)")
        print("0. Tillbaka till byn")
        choice = input("Ditt val: ")

        if choice == "1":
            print(buy_weapon(player, "Träsvärd"))
        elif choice == "2":
            print(buy_weapon(player, "Järnsvärd"))
        elif choice == "0":
            current_scene = "village"
        else:
            print("Välj ett av alternativen.")

    elif current_scene == "bridge":
        print("\nDu kommer fram till bron. Vad händer här?")
        print("Den här scenen ska du själv utveckla.")
        print(f"En magisk spell hindrar {player["name"]} från att nå bron .", end="", flush=True)
        for i in range(5):
            time.sleep(1)
            print(" .", end="", flush=True)
        clear_screen()
        current_scene = "village"

print("Äventyret är slut.")
