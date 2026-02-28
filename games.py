import inputs
import time

from prettytable import PrettyTable

# Nonami Launcher

def launch():
    while True:
        cmd = input("-> ")
        if cmd == "gl":
            games_list()
        elif cmd == "help":
            aide()
        elif cmd == "math5":
            math5()
        elif cmd == "cd":
            break
        elif cmd in ["stop", "st"]:
            inputs.stop()
        else:
            inputs.illegal()

def games_list():
    table = PrettyTable()
    table.field_names = ["Jeux", "Description"]
    table.add_row(["math5", "Un simple jeu de Maths !"])
    print(table)
    time.sleep(0.5)

def aide():
    print("Faites gl pour voir la liste des jeux disponibles.")

def math5():
    print("Math5 game...")
    import math5 as logic
    logic.launcher()