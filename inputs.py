# Commands File
import os
import random
import time
import platform
import sounddevice as sd
import soundfile as sf
import sys

from prettytable import PrettyTable

# "Code of commands"
def start():
    print("Game start...")
    play("start.wav")

def stop():
    print("Game close...")
    play("stop.wav")
    sys.exit(0)

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS  # dossier temporaire PyInstaller
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()

def play(filename):
    path = os.path.join(BASE_DIR, "musique", filename)
    data, fs = sf.read(path)
    sd.play(data, fs)
    sd.wait()

def command_list():
    table = PrettyTable()
    table.field_names = ["Command name", "Typing", "Utilities"]
    table.add_row(["Command List", "cl", "Montre les différentes commandes"])
    table.add_row(["Command", "cd", "Donne la possibilité de fare des commandes"])
    table.add_row(["Jeux", "games", "Montre les jeux disponibles"])
    table.add_row(["Arrêt", "stop", "Met fin au code"])
    table.add_row(["Calculator", "cal", "Permet des calculs avec une calculatrice"])
    table.add_row(["Direct cal.", "dcal", "Part directement dans la calculatrice"])
    table.add_row(["Astuce", "atc", "Donne des astuces ou conseils"])
    table.add_row(["Faits", "fact", "Donne des faits interresants de Nonami"])
    table.add_row(["Get-time", "gtime", "Donne le temps"])
    table.add_row(["Code Morse", "morse", "Traduit en Morse les entrées"])
    table.add_row(["Devapps", "apps", "Montre les applications en développement"])
    print(table)
    time.sleep(0.5)

def commands():
    while True:
        command = input(">")
        if command in ["jeux", "games"]:
            jeux()
        elif command in ["command_list", "cl"]:
            command_list()
        elif command in ["stop", "st"]:
            stop()
        elif command in ["reload"]:
            reload()
        elif command in ["devapps", "dev", "apps"]:
            devapps()
        elif command in ["commands", "cd",]:
            print()
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
            play("error.wav")
            print("Cette commande est inexistante.")
            play("error.wav")
            print()

def jeux():
    import games as logic
    logic.launch()

def devapps():
    import devapps as logic
    logic.menu()

def get_time():
    ac_clock = time.ctime()
    print(f"{ac_clock} est votre heure actuelle.")

def calculator():
    time.sleep(1)
    print()
    cal_rules()

def math_lines():
    while True:
        a = input("~")
        if a.lower() == "stop":
            stop()
            break
        elif a.lower() == "pop":
            poss_op()
            break
        elif a.lower() == "cd":
            break
        else:
            try:
                result = eval(a)
                print("»", result)
                time.sleep(1)
            except Exception as e:
                print("Calculator Error : ", e)

def poss_op():
    print("""Voici quelques posibilités d'opération:
    +  | Additionne deux nombres;
    -  | Soustrait deux nombres;
    *  | Multiplie deux nombres;
    /  | Divise deux nombres;
    ** | Élève un nombre à une puissance.""")
    time.sleep(0.5)
    print("Besoin d'aide, faites pop.")
    print("Faites cd pour revenir aux commandes normales ou stop pour tout arrêter.")
    math_lines()

def astuces():
    table = PrettyTable()
    print()
    time.sleep(0.5)
    print("Voici un conseil ou une astuce !")

    astuce = random.randint(1, 10)
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
        table.add_row(["->", "Vous êtes dans le Launcher de jeux."])
        table.add_row([">>>", "Vous êtes dans le menu des applications en développement."])
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
    elif astuce == 10:
        print("Vous voulez faire crash Nonami ? Allez testez les applications en développement !")
    else:
        illegal()

def facts():
    print()
    time.sleep(0.5)
    print("Voici un fait sur Nonami !")

    fact = random.randint(1, 27)
    if fact == 1:
        print("Le créateur de Nonami a aussi créé Transcriptor.")
    elif fact == 2:
        print("Nonami est dans sa version: 0.5. Imaginez que ce texte doit changer chaque fois (il est unique).")
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
        print("Les versions plus que mineures (c'est une appellation) comme ceci x.x.0 (représentées par le 0) est, pour le moment, juste des corrections de bugs.")
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
        print("Il y a 25 faits en tout (+ celui-ci) !")
    elif fact == 21:
        print("Le son d'introduction de Nonami a été imaginé du jour au lendemain !")
    elif fact == 22:
        print("La traduction en Morse a été ajouté au cours du développement de la version 0.4.8 !")
    elif fact == 23:
        print("Nonami a été fait pour être un projet de programmation amusant, mais aussi pour apprendre et s'améliorer en Python !")
    elif fact == 24:
        print("Le Laucher de jeux et les applications en développement ont été ajoutés à la version majeure 0.5. Allez les tester !")
    elif fact == 25:
        print("Il existe des commandes secrètes... ne crackez pas le code pour les trouver, svp...")
    elif fact == 26:
        print("Une toute nouvelle bibliothèque de sons a été ajoutée à Nonami pour la version 0.5 !")
    elif fact == 27:
        print("De noumbreuses optimisations ont été faites pour la version 0.5, notamment pour les commandes et les jeux !")
    else:
        illegal()

def clear():
    # Efface l'écran de la console de façon portable.
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

def illegal():
    print("Hooo, ça n'a pas fonctionné. »»» Sortie de code.")
    play("illegal.wav")
    print()

def code1():
    while True:
        strt = input("Write here: ")
        if strt in ["start", "strt"]:
            start()
            break
        elif strt in ["stop", "st"]:
            stop()
        else:
            play("error.wav")
            print("Ceci n'est pas dans les choix. Faites *stop* ou *st* (sans les stars) pour quitter.")
            play("error.wav")
            time.sleep(1)

def cal_rules():
    rule = input("Voulez-vous voir les instructions de calculator ? (y/n)> ")
    time.sleep(0.5)
    if rule == "y":
        print("""
        Règlement...
        Vous devez uniquement utiliser des fonction des maths pour faire vos opérations.
        Vos opérations doivent être seulement dans une ligne.
        Besoin d'aide, faites pop.
        Si vous voulez quitter, faites cd pour menu principal.
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
    play("intro.wav")

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
        if text.lower() == "stop":
            stop()
            break
        elif text.lower() == "cd":
            break
        else:
            try:
                encoded_text = encode_morse(text)
                print(encoded_text)
                for char in encoded_text:
                    if char == '.':
                        play("dot.wav")
                    elif char == '-':
                        play("dash.wav")
                    elif char == ' ':
                        time.sleep(0.25)
                    # Ajoutez d'autres sons Morse au besoin
            except Exception as e:
                print("Traduction Error : ", str(e))
