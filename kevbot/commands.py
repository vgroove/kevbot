from random import randint

def roll(*args):
    """Rolls a die with the number of sides specified"""
    try:
        sides = int(args[0])
    except:
        return "I need an integer if you want me to roll these dice."
    return "The result is...{0}!".format(randint(1, sides))
