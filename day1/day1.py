import re


def partie1(lignes):
    pattern = r'\d'
    somme = 0
    for ligne in lignes:
        chaine = re.findall(pattern, ligne)
        somme += int(chaine[0] + chaine[-1])

    return somme


def sequence_to_chiffre(lettre):
    correspondance = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                      'eno': 1, 'owt':2, 'eerht': 3, 'ruof': 4, 'evif':5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
    return str(correspondance.get(lettre, 0))


def partie2(lignes):
    pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
    patternr = r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
    somme = 0
    for ligne in lignes:
        st = ""
        chaine = re.search(pattern, ligne)
        chaine1 = re.search(patternr, ligne[::-1])
        chaine = chaine.group()
        chaine1 = chaine1.group()
        if chaine.isdigit():
            st += chaine
        else:
            st += sequence_to_chiffre(chaine)

        if chaine1.isdigit():
            st += chaine1
        else:
            st += sequence_to_chiffre(chaine1)

        somme += int(st)

    return somme


if __name__ == '__main__':
    file = open("input.txt", "r")
    lignes = file.readlines()
    print(f"partie 1 : {partie1(lignes)}")
    print(f"partie 2 : {partie2(lignes)}")