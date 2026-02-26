import inputs
import random

def launcher():
    print("Bienvenue dans Math5 ! Un simple jeu de Maths !")

    while True:
        math5_rule = input("Voulez-vous voir le règlement ? (y/n): ")
        if math5_rule == "y":
            print("""Vous devez saisir une liste de 5 nombres dont la somme est égal de ce nombre.
            Vous n'avez pas le droit de mettre la même somme que celle donnée ou de mettre un 0.
            Avez-vous compris ? (y/n)""")
            rep = input('Rep: ')
            if rep == 'y':
                print('Bien...')
                code()
                break
            else:
                inputs.bye()
        elif math5_rule == "n":
            code()
            break
        else:
            print("Ceci n'est pas dans les choix de réponse.\n")

    while True:
        repp = input("\nVoulez-vous recommencer ? (y/n): ")
        if repp == "y":
            code()
        elif repp == "n":
            break
        else:
            print("Ceci n'est pas dans les choix de réponse.\n")

def code():
    NOM = random.randint(5, 1000000)
    print(f"\n{NOM} est le nombre !")

    numbers = []
    while len(numbers) < 5:
        try:
            num = float(input(f"Nombre {len(numbers)+1}: "))
            if num == 0 or num == NOM:
                print("Tricher, c'est mal! Recommence.\n")
                continue
            numbers.append(num)
        except ValueError:
            print("Non, un vrai nombre!\n")

    total = sum(numbers)
    if total == NOM:
        print("Bravo, vous avez réussi !")
    else:
        print(f"Raté. {total} n'est pas égal à {NOM}.")

launcher()