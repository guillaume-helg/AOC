import re

def partie1(lignes):
    pattern = r'[^\w\s\.]'
    patternc = r'\d+'
    somme = 0
    correspondances = re.findall(pattern, lignes)
    for chaine in correspondances:
        match = re.search(patternc, chaine)
        somme += int(match.group())

    return somme




def partie2(lignes):
    print("hello")


if __name__ == '__main__':
    file = open("input.txt", "r")
    contenu = file.read()
    print(f"partie 1 : {partie1(contenu)}")
    print(f"partie 2 : {partie2(contenu)}")