def partie1(lignes):
    return lignes.count("(") - lignes.count(")")



def partie2(lignes):
    a = 0
    b = 0
    index = 0
    for char in lignes:
        index += 1
        if char == "(":
            a += 1
        else:
            b += 1
            if b > a:
                return index

    return 0


if __name__ == '__main__':
    file = open("input.txt", "r")
    lignes = file.read()
    print(f"partie 1 : {partie1(lignes)}")
    print(f"partie 2 : {partie2(lignes)}")