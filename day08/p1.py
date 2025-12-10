import sys
from collections import Counter
from math import prod

class Circuit:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        x, y = self.find(x), self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


def main() -> None:
    junctions = open(sys.argv[1]).read().splitlines()
    junctions = [tuple(map(int, junction.split(","))) for junction in junctions]
    n = len(junctions)
    circuit = Circuit(n)

    distances = []

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = junctions[i]
            x2, y2, z2 = junctions[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((dist, i, j))

    distances.sort()

    for idx, (_, junc1, junc2) in enumerate(distances):
        if idx >= 1000:
            break
        circuit.union(junc1, junc2)

    c = Counter(circuit.find(i) for i in range(n))
    print(prod(count for _, count in c.most_common(3)))


if __name__ == "__main__":
    main()
