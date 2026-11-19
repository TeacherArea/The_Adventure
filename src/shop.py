# Regler för shoppen.
# Inga utskrifter eller användarfrågor här.

def buy_weapon(player, weapon_name):
    if weapon_name == "Träsvärd":
        price = 5
        required_exp = 0
    elif weapon_name == "Järnsvärd":
        price = 15
        required_exp = 10
    else:
        return "Det vapnet finns inte."

    if weapon_name in player["weapons"]:
        return "Du har redan det vapnet."
    if player["experience"] < required_exp:
        return "Du har för lite erfarenhet."
    if player["gold"] < price:
        return "Du har inte tillräckligt med guld."

    player["gold"] -= price
    player["weapons"].append(weapon_name)
    return f"Du köpte {weapon_name}!"
