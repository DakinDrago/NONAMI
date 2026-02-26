# Commands File
import os
import random
import subprocess
import time
import platform
import winsound

# from playsound import playsound
from prettytable import PrettyTable

# "Code of commands"
def start():
    print("Game start...")
    winsound.Beep(1567, 750)

def stop():
    winsound.Beep(784, 333)
    print("Game close...")
    winsound.Beep(1174, 333)
    winsound.Beep(1568, 333)
    time.sleep(1)
    exit("Finish.")

def command_list():
    table = PrettyTable()
    table.field_names = ["Command name", "Typing", "Utilities"]
    table.add_row(["Command List", "cl", "Montre les différentes commandes"])
    table.add_row(["Command", "cd", "Donne la possibilité de fare des commandes"])
    table.add_row(["Play", "game", "Montre les jeux disponibles"])
    table.add_row(["Arrêt", "stop", "Met fin au code"])
    table.add_row(["Calculator", "cal", "Permet des calculs avec une calculatrice"])
    table.add_row(["Direct cal.", "dcal", "Part directement dans la calculatrice"])
    table.add_row(["Astuce", "atc", "Donne des astuces ou conseils"])
    table.add_row(["Faits", "fact", "Donne des faits interresants de Nonami"])
    table.add_row(["Get-time", "gtime", "Donne le temps"])
    table.add_row(["Code Morse", "morse", "Traduit en Morse les entrées"])
    print(table)
    time.sleep(0.5)
    commands()

def commands():
    command = input(">")
    if command in ["jeux", "game"]:
        jeux()
    elif command in ["command_list", "cl"]:
        command_list()
    elif command in ["stop", "st"]:
        stop()
    elif command in ["reload"]:
        reload()
    elif command == "math5":
        math5()
    elif command in ["commands", "cd",]:
        print()
        commands()
    elif command in ["astuce", "atc"]:
        astuces()
    elif command == "fact":
        facts()
    elif command == "morse":
        morse()
    elif command in ["gtime", "time"]:
        get_time()
    elif command in ["calculator", "cal"]:
        calculator()
    elif command == "dcal":
        math_lines()
    elif command == "clear":
        clear()
    else:
        winsound.Beep(1318, 100)
        print("Cette commande est inexistante.")
        winsound.Beep(1318, 100)
        print()
        commands()

def math5():
    print("Math5 game...")
    import math5 as logic
    logic.launcher()
    commands()

def jeux():
    print("""Si vous voulez retourner au menu principal, faites cd.
    Voici la liste des jeux disponibles:
    Math5 (ex. math5).""")
    jeux_rep = input("Rep: ")
    if jeux_rep == "math5":
        math5()
    elif jeux_rep == "cd":
        commands()
    else:
        illegal()

def get_time():
    ac_clock = time.ctime()
    print(f"{ac_clock} est votre heure actuelle.")
    commands()

def calculator():
    time.sleep(1)
    print()
    cal_rules()

def math_lines():
    while True:
        a = input("~")
        if a.lower() == "bye":
            bye()
            break
        elif a.lower() == "stop":
            stop()
            break
        elif a.lower() == "pop":
            poss_op()
            break
        elif a.lower() == "cd":
            commands()
            break
        else:
            try:
                result = eval(a)
                print("»", result)
                time.sleep(1)
            except Exception as e:
                print("Calculator Error : ", e)
        math_lines()

def poss_op():
    print("""Voici quelques posibilités d'opération:
    +  | Additionne deux nombres;
    -  | Soustrait deux nombres;
    *  | Multiplie deux nombres;
    /  | Divise deux nombres;
    ** | Élève un nombre à une puissance.""")
    time.sleep(0.5)
    print("Besoin d'aide, faites pop.")
    print("Faites cd pour revenir aux commandes normales, bye pour voir d'autres jeux et stop pour tout arrêter.")
    math_lines()

def astuces():
    table = PrettyTable()
    print()
    time.sleep(0.5)
    print("Voici un conseil ou une astuce !")

    astuce = random.randint(1, 9)
    if astuce == 1:
        print("""Faites attention avec la commande (cl) et (clear). Ce n'est pas la même chose !
        cl revient aux commandes alors que clear efface TOUT.""")
    elif astuce == 2:
        print("N'écrivez rien en majuscule (pour une fois) !")
    elif astuce == 3:
        table.field_names = ["Signe", "Definition"]
        table.add_row([">", "Vous êtes aux commandes."])
        table.add_row(["~", "Vous êtes dans calculator."])
        table.add_row(["£", "Vous êtes dans le jeux Morse."])
        print(table)
    elif astuce == 4:
        print("Entraînez-vous sur Math5 pour devenir fort en addition.")
    elif astuce == 5:
        print("Sur Nonami, vous n'avez pas besoin de curseur. Tout ce fait avec texte !")
    elif astuce == 6:
        print("Hey, stop = st et start = strt. Now, no errors.")
    elif astuce == 7:
        print("Faites en sorte d'écire la commande au complet (l'abréviation de celle-ci incluse) !")
    elif astuce == 8:
        print("Nonami n'aime pas trop lorsqu'on le 'down'. Faites pluto la commande stop lorsqu'elle est disponible.")
    elif astuce == 9:
        print("Dans Morse, utilisez tous les caractères graphiques (é,ï,ç), ils fonctionneront !")
    else:
        illegal()
    commands()

def facts():
    print()
    time.sleep(0.5)
    print("Voici un fait sur Nonami !")

    fact = random.randint(1, 22)
    if fact == 1:
        print("Le créateur de Nonami a aussi créé Transcriptor.")
    elif fact == 2:
        print("Nonami est dans sa version: 0.4.9 . Imaginez que ce texte doit changer chaque fois (il est unique).")
    elif fact == 3:
        print("Savez-vous que Nonami a commencé seulement à partir de Math5, qui lui s'appelait autre fois juste Math ?")
    elif fact == 4:
        print("Nonami a failli se nommer Nanomi (il peut toujours le devenir)... c'est incroyable, non ?")
    elif fact == 5:
        print("Le projet Nonami a commencé vers les environs d'Octobre 2023.")
    elif fact == 6:
        print("Nonami a été fait à 97% par un humain, 2% par GPT-3.5, GPT-4o, GPT-5.2 et 1% par Claude.")
    elif fact == 7:
        print("Si vous ne l'avez pas déjà remarqué, Nonami ressemble à une sorte d'OS (operating system)")
    elif fact == 8:
        print("""Le code de Nonami est organisé comme ceci:
    Une sorte de grande bibliothèque dont les instructions des livres (codes) sont inscrits sur une feuille qui indique tous les différents livres (main).""")
    elif fact == 9:
        print("Les facts (faits) ont été ajouté à Nonami sur la version mineure: 0.4.7 .")
    elif fact == 10:
        print("Calculator est directement lié à Python. Il a été ajouté à la version mineure: 0.3.2 .")
    elif fact == 11:
        print("Les versions plus que mineures (c'est une appellation) comme ceci x.x.x.0 (représentées par le 0) est, pour le moment, juste des corrections de bugs.")
    elif fact == 12:
        print("J'espère que la commande facts fonctionnera... Ouups !?! ... ça ne doit pas être ici !")
    elif fact == 13:
        print("La difficulté de Math5 peut être modifiée... alors attention !")
    elif fact == 14:
        print("Nonami ne restera pas éternellement en Français... il y aura d'autres versions.")
    elif fact == 15:
        print("La fonction la plus utilisée sur facts est elif.")
    elif fact == 16:
        print("La fonction la plus utilisée sur Nonami est def (abréviation).")
    elif fact == 17:
        print("Beaucoup de gens me disent: « Tu mets tout le temps des points aux phrases lorsque tu clavardes ! ». Donc, cette fois ci, je ne vais pas en mettre")
    elif fact == 18:
        print("La commande clear cause beaucoup de soucis.")
        print("Voyez-le par vous-même dans 3 secondes.")
        time.sleep(0.5)
        print("Est-ce que ça va vraiment clear ?")
        time.sleep(2.5)
        clear()
    elif fact == 19:
        print("Vous vous demandez surement: « Qu'est-ce qu'est 𝕷𝖊 𝕯𝖔𝖈𝖚𝖒𝖊𝖓𝖙𝖆𝖎𝖗𝖊 ? ».")
        time.sleep(0.25)
        print("𝕷𝖊 𝕯𝖔𝖈𝖚𝖒𝖊𝖓𝖙𝖆𝖎𝖗𝖊 est une (future) entreprise d'information mondiale. Voilà.")
    elif fact == 20:
        print("Il y a 22 faits en tout (+ celui-ci) !")
    elif fact == 21:
        print("Le son d'introduction de Nonami a été imaginé du jour au lendemain !")
    elif fact == 22:
        print("La traduction en Morse a été ajouté au cours du développement de la version 0.4.8 !")
    else:
        illegal()
    commands()

def clear():
    """Efface l'écran de la console de façon portable."""
    system = platform.system()

    if system == 'Windows':
        os.system('cls')
    elif system in ['Linux', 'Darwin']:  # Linux ou macOS
        os.system('clear')
    else:
        # Solution alternative pour les systèmes non reconnus
        print("\n" * 100)  # Imprime plusieurs lignes vides

    time.sleep(1)
    print("La console a été clear.")
    commands()

def bye():
    print("Vous voulez sortir du jeu ?")
    time.sleep(0.5)
    print("""Il y a d'autres jeux ! Faites jeux.""")
    time.sleep(1)
    print("Vous voulez quitter ? Faites stop ou st.")
    print("Voulez-vous revenir au menu principal ? Faites: cd.")

    def bye_rep():
        return input("Rep: ")

    response = bye_rep()
    if response == "jeux":
        jeux()
    elif response in ["stop", "st"]:
        stop()
    elif response == "cd":
        commands()
    else:
        print("Ceci n'est pas dans les choix.")
        time.sleep(1)
        print()
        bye_rep()

def illegal():
    winsound.Beep(784, 333)
    print("Hooo, ça n'a pas fonctionné. »»» Sortie de code.")
    winsound.Beep(784, 333)
    winsound.Beep(784, 333)
    print()
    commands()

def code1():
    strt = input("Write here: ")
    if strt in ["start", "strt"]:
        start()
    elif strt in ["stop", "st"]:
        stop()
    else:
        winsound.Beep(1318, 100)
        print("Ceci n'est pas dans les choix. Faites *stop* ou *st* (sans les stars) pour quitter.")
        winsound.Beep(1318, 100)
        time.sleep(1)
        code1()

def cal_rules():
    rule = input("Voulez-vous voir les instructions de calculator ? (y/n)> ")
    time.sleep(0.5)
    if rule == "y":
        print("""
        Règlement...
        Vous devez uniquement utiliser des fonction des maths pour faire vos opérations.
        Vos opérations doivent être seulement dans une ligne.
        Besoin d'aide, faites pop.
        Si vous voulez quitter, faites bye ou cd pour menu principal.
        """)
        time.sleep(2)
        print("""Voici quelques posibilités d'opération:
                +  | Additionne deux nombres;
                -  | Soustrait deux nombres;
                *  | Multiplie deux nombres;
                /  | Divise deux nombres;
                ** | Élève un nombre à une puissance.
                """)
        math_lines()
    else:
        poss_op()

def reload():
    import sys
    os.execv(sys.executable, ["python"] + sys.argv)

def intro():
    import winsound
    winsound.Beep(587, 200)
    winsound.Beep(587, 200)
    winsound.Beep(587, 200)
    winsound.Beep(493, 200)
    winsound.Beep(523, 200)
    winsound.Beep(493, 200)
    winsound.Beep(440, 200)
    winsound.Beep(392, 200)

def morse():
    morse_code = {
        'A': '.-', 'Ä': '.-.-', 'Æ': '.-.-', 'À': '.--.-', 'Å': '.--.-', 'B': '-...', 'C': '-.-.', 'Ĉ': '-.-..', 'Ç': '-.-..',
        'CH': '----', 'D': '-..', 'Ð': '..--.', 'E': '.', 'É': '..-..', 'È': '.-..-', 'F': '..-.', 'G': '--.', 'Ĝ': '--.-.',
        'H': '....', 'Ĥ': '-.--.', 'I': '..', 'J': '.---', 'Ĵ': '.---.', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'Ñ': '--.--', 'O': '---', 'Ö': '---.', 'Ø': '---.', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'Ŝ': '...-.',
        'T': '-', 'Þ': '.--..', 'U': '..-', 'Ü': '..--', 'Ŭ': '..--', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', ' ': '/', '@': '.--.-.'
    }

    def encode_morse(morse_text):
        encoded_text = ''
        for char in morse_text.upper():
            if char in morse_code:
                encoded_text += morse_code[char] + ' '
        return encoded_text.strip()

    while True:
        text = input("£ ")
        if text.lower() == "bye":
            bye()
            break
        elif text.lower() == "stop":
            stop()
            break
        elif text.lower() == "cd":
            commands()
            break
        else:
            try:
                encoded_text = encode_morse(text)
                print(encoded_text)
                for char in encoded_text:
                    if char == '.':
                        winsound.Beep(1174, 250)
                    elif char == '-':
                        winsound.Beep(1174, 600)
                    elif char == ' ':
                        time.sleep(0.25)
                    # Ajoutez d'autres sons Morse au besoin
            except Exception as e:
                print("Traduction Error : ", str(e))
