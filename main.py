import inputs
import sys
import os

# Force l'ouverture dans une console si double-cliqué
if getattr(sys, 'frozen', False) and sys.stdin is None:
    os.system('start cmd /k "' + sys.executable + '"')
    sys.exit()

# Accueil
print("""███╗   ██╗ ██████╗ ███╗   ██╗ █████╗ ███╗   ███╗██╗
████╗  ██║██╔═══██╗████╗  ██║██╔══██╗████╗ ████║██║
██╔██╗ ██║██║   ██║██╔██╗ ██║███████║██╔████╔██║██║
██║╚██╗██║██║   ██║██║╚██╗██║██╔══██║██║╚██╔╝██║██║
██║ ╚████║╚██████╔╝██║ ╚████║██║  ██║██║ ╚═╝ ██║██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝
𝕷𝖊 𝕯𝖔𝖈𝖚𝖒𝖊𝖓𝖙𝖆𝖎𝖗𝖊                                 [?]
""")
inputs.intro()
print("""Bienvenue sur Nonami v0.5.1, un logiciel qui pour l'instant... ne fait pas grand chose, mais qui a de grandes ambitions !
Si vous êtes nouveau, faites start ou strt.""")

# Code1
rep = inputs.code1()
print()

print("""Bienvenue ! Ici vous pourrez faire des jeux et activités !
Faites cl pour commencer.""")
inputs.commands()