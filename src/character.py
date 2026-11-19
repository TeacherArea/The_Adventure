# Skapar spelaren när ett nytt äventyr börjar.
# Detta är ett exempel på en dictionary, som innehåller olika typer och två tomma listor.
# Inga utskrifter eller användarfrågor här.

def create_player(name):
    return {
        "name": name,
        "gold": 20,
        "strength": 5,
        "experience": 0,
        "weapons": [],
        "artifacts": [],
    }
