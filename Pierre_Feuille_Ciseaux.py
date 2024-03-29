#coding: UTF-8
from random import choice

# liste de coups
coups = ["pierre", "feuille", "ciseaux"]

# a est l'ordi
cpu = "Ordi"

# b est le joueur
joueur = "Joueur"


# coup ordi
def coup_CPU():
    return choice(coups)


# coup joueur
def coup_joueur():
    Joueur = input("Votre tour : ")
    for i, nom in enumerate(coups):
        if Joueur in [str(i + 1), nom[0], nom]:
            return nom
    return False


# compteur
score_joueur = 0
score_cpu = 0


# comparaison coup
def comp(a, b):
    global score_joueur, score_cpu
    if a == b:
        print("Egalité")
    elif a == "pierre":
        if b == "feuille":
            print(f"{joueur} gagne")
            score_joueur += 1
        elif b == "ciseaux":
            print(f"{cpu} gagne")
            score_cpu += 1

    elif a == "feuille":
        if b == "pierre":
            print(f"{cpu} gagne")
            score_cpu += 1
        elif b == "ciseaux":
            print(f"{joueur} gagne")
            score_joueur += 1

    elif a == "ciseaux":
        if b == "pierre":
            print(f"{joueur} gagne")
            score_joueur += 1
        elif b == "feuille":
            print(f"{cpu} gagne")
            score_cpu += 1


# lancement
lancement = False


def start():
    global lancement
    lancement = True


# début
start()
while lancement:
    JOUEUR = coup_joueur()
    CPU = coup_CPU()
    if JOUEUR == False:
        print("erreur")
        continue
    print(f"Vous avez joué {JOUEUR} \nl'ordi à joué {CPU}")
    comp(CPU, JOUEUR)
    
# score
    print(f"- ordi = {score_cpu} point")
    print(f"- joueur = {score_joueur} point")

# message victoire
    if score_joueur >= 5:
        print(f"Victoire de {joueur}")
        lancement = False
    elif score_cpu >= 5:
        print(f"Victoire de {cpu}")
        lancement = False
