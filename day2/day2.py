import re
def partie1(lignes):
    pattern_blue = r'\d+ blue'
    pattern_green = r'\d+ green'
    pattern_red = 'r\d+ red'
    somme = 0
    # pour chaque ligne
    # je verifie si y'a 12 cube rouge et 13 cubes vert et 14 cubes bleu
    # si oui j'additionne l'id de la game à la somme, sinon non
    for ligne in lignes:



    somme += id


def partie2(lignes):
    print("hola")


if __name__ == '__main__':
    file = open("input.txt", "r")
    lignes = file.readlines()
    print(f"partie 1 : {partie1(lignes)}")
    print(f"partie 2 : {partie2(lignes)}")
