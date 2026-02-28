import inputs
import time

from prettytable import PrettyTable

def menu():
    while True:
        launch = input(">>> sudo ")
        if launch == "al":
            apps_list()
        elif launch in ["help", "aide"]:
            aide()
        elif launch == "pfc":
            pfc()
        elif launch == "110":
            de1à10()
        elif launch == "cb":
            compte_bancaire()
        elif launch == "cd":
            break
        elif launch in ["stop", "st"]:
            inputs.stop()
        else:
            inputs.illegal()

def apps_list():
    table = PrettyTable()
    table.field_names = ["Applications", "Description"]
    table.add_row(["pfc", "Pierre, Feuille, Ciseaux"])
    table.add_row(["110", "Devinez un nombre entre 1 et 10"])
    table.add_row(["cb", "Gestion de votre compte bancaire"])
    print(table)
    time.sleep(0.5)

def aide():
    print("Faites al pour voir la liste des applications disponibles.")
    print("Attention, certaines applications sont encore en développement !")

def pfc():
    import cours3 as logic
    logic.pfc()

def de1à10():
    import cours3 as logic
    logic.de1à10()

def compte_bancaire():
    import cours3 as logic
    logic.compte_bancaire()