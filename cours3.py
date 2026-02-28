#import devapps
import random

def pfc():
    print("Bienvenue dans Pierre, Feuille, Ciseaux !")
    print("Roche, papier, ciseau (et allumettes!)")
    print("Qu'est-ce que tu vas mettre dans ton assiette...")
    print("..1 (entrez R pour roche)")
    print("..2 (entrez P pour papier)")
    print("..3 (entrez C pour ciseau)")

    def logic(a, b):
        if a == b:
            print("Égalité!")
        elif a == "r" and b == "c":
            print("Tu as gagné")
            pass
        elif a == "p" and b == "r":
            print("Tu as gagné")
            pass
        elif a == "c" and b == "p":
            print("Tu as gagné")
        else:
            if b == "r":
                print("C'était une roche.")
            elif b == "p":
                print("C'était un papier.")
            else:
                print("C'était un ciseau.")
        print("Encore!")

    for Cameroon in range(5):
        # User
        a = input("GO! > ")

        # Machine
        prob = ["r", "p", "c"]
        b = random.choice(prob)

        # Fonction
        logic(a, b)

def de1à10():
    def check_answer(choix, reponse):
        if choix == reponse:
            print("message")
        else:
            print("message 2")

    reponse = 8

    for i in range(1):
        choix = int(input("Choisi un nombre entre 1 et 10: "))
        check_answer(choix, reponse)


def compte_bancaire():
    balance = 1350

    def ajouter(monnaie, qte):
        solde = monnaie + qte
        return solde

    def retirer(monnaie, qte):
        solde = monnaie - qte
        if monnaie < qte:
            print("Fraudeur!")
        else:
            return solde
        
    print("Salut, ajouter (a) ou retirer de l'argent (r) ?")
    while True:
        input("> ").lower
        if input == "a":
            ajouter()
        elif input == "r":
            retirer()
        else:
            print("Quoi?")