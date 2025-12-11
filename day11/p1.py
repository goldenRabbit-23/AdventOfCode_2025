import sys
from functools import cache


def main() -> None:
    data = open(sys.argv[1]).read().splitlines()
    graph = {}

    for line in data:
        src, dsts = line.split(':')
        graph[src] = dsts.split()

    @cache
    def dfs(current) -> int:
        if current == "out":
            return 1

        total = 0

        for neigh in graph[current]:
            total += dfs(neigh)

        return total

    print(dfs("you"))


if __name__ == "__main__":
    main()
