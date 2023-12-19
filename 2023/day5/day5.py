def partie1(lines):
    seeds, *mappings = lines.split("\n\n")
    # i have the seed
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]

    # i need the mappings
    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

        def translate(x):
            for a, b in ranges:
                if x in b:
                    return a.start + x - b.start
            return x

        seeds = [translate(x) for x in seeds]

    return min(seeds)

def partie2(lines):
    seeds, *mappings = lines.split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]

    new_seeds = []
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for a, b in seeds:
        c = a
        while c <= a + b:
            new_seeds.append(c)
            c += 1

    print(new_seeds)

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

        def translate(x):
            for a, b in ranges:
                if x in b:
                    return a.start + x - b.start
            return x

        new_seeds = [translate(x) for x in new_seeds]

    return min(new_seeds)



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read()
    print(f"partie 1 : {partie1(lines)}")
    print(f"partie 2 : {partie2(lines)}")