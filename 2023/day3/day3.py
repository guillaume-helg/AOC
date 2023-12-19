import re
from collections import defaultdict


def partie1(lines):
    ans = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            count = sum(0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "." for a, b in idxs)
            if count > 0:
                ans += int(m.group())
    return ans


def partie2(lines):
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] == "*":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    print(f"partie 1 : {partie1(lines)}")
    print(f"partie 2 : {partie2(lines)}")