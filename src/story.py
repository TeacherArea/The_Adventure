# Korta berättelsetexter, men ingen input() eller print() här bara return till show.py.

# ta bort clear_screen() när du inte behöver den längre, den ska inte finnas här
def clear_screen():
    print("\033[2J\033[H", end="", flush=True)

def village_intro(name):
    return f"{name} står på torget i en liten by."


def shop_intro():
    return "I affären säljs ett träsvärd och ett järnsvärd."