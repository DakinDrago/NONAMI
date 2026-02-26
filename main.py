import inputs
import time

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
time.sleep(1)
print("""Bienvenue sur Nonami v0.4.9, un logiciel qui pour l'instant...
Si vous êtes nouveau, faites start ou strt.""")

# Code1
rep = inputs.code1()
time.sleep(1)
print()

print("""Bienvenue ! Ici vous pourrez faire des jeux et activités !
Faites cl pour commencer.""")
inputs.commands()