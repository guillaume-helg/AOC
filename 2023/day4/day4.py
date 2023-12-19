import re
from collections import defaultdict


def partie1(lines):
    sum = 0
    for line in lines:
        line = line.split('|')
        db = 0
        for m in re.finditer(r"\d+", line[1]):
            lit = line[0].split(':')
            lit = lit[1].split(' ')
            if m.group() in lit:
                if db == 0:
                    db = 1
                else:
                    db = db * 2

        sum += db
    return sum


def partie2(lines):
    total_sum = 0
    i = 0
    while i < len(lines):
        line = lines[i].split('|')
        db = 0
        for m in re.finditer(r"\d+", line[1]):
            lit = line[0].split(':')
            lit = lit[1].split(' ')
            if m.group() in lit:
                db += 1

        rota = db
        j = i + 1
        while j < i + rota and j < len(lines):
            line = lines[j].split('|')
            for m in re.finditer(r"\d+", line[1]):
                lit = line[0].split(':')
                lit = lit[1].split(' ')
                if m.group() in lit:
                    db += 1
            j += 1

        total_sum += db
        i += 1

    return total_sum



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(f"partie 1 : {partie1(lines)}")
    print(f"partie 2 : {partie2(lines)}")
