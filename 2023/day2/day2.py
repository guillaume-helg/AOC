import re


def partie1(lignes):
    pattern_blue = r'\d+ blue'
    pattern_green = r'\d+ green'
    pattern_red = r'\d+ red'
    somme = 0
    i = 0
    for ligne in lignes:
        chaine_red = re.findall(pattern_red, ligne)
        chaine_bleu = re.findall(pattern_blue, ligne)
        chaine_green = re.findall(pattern_green, ligne)
        max_red = max(int(item.split()[0]) for item in chaine_red)
        max_green = max(int(item.split()[0]) for item in chaine_green)
        max_blue = max(int(item.split()[0]) for item in chaine_bleu)
        i += 1

        if max_green <= 13 and max_blue <= 14 and max_red <= 12:
            somme += i

    return somme


def partie2(lignes):
    pattern_blue = r'\d+ blue'
    pattern_green = r'\d+ green'
    pattern_red = r'\d+ red'
    somme = 0
    for ligne in lignes:
        chaine_red = re.findall(pattern_red, ligne)
        chaine_bleu = re.findall(pattern_blue, ligne)
        chaine_green = re.findall(pattern_green, ligne)
        somme_red = max(int(item.split()[0]) for item in chaine_red)
        somme_green = max(int(item.split()[0]) for item in chaine_green)
        somme_blue = max(int(item.split()[0]) for item in chaine_bleu)
        somme += somme_blue * somme_red * somme_green

    return somme


if __name__ == '__main__':
    file = open("input.txt", "r")
    lignes = file.readlines()
    print(f"partie 1 : {partie1(lignes)}")
    print(f"partie 2 : {partie2(lignes)}")
