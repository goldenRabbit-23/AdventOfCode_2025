import sys
from functools import cache


def main() -> None:
    data = open(sys.argv[1]).read().splitlines()
    graph = {}

    for line in data:
        src, dsts = line.split(':')
        graph[src] = dsts.split()

    @cache
    def dfs(current, target) -> int:
        if current == target:
            return 1

        if current not in graph:
            return 0

        return sum(dfs(neigh, target) for neigh in graph[current])

    # Scenario 1: svr -> dac -> fft -> out
    scenario1 = dfs("svr", "dac") * dfs("dac", "fft") * dfs("fft", "out")

    # Scenario 2: svr -> fft -> dac -> out
    scenario2 = dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")

    print(scenario1 + scenario2)


if __name__ == "__main__":
    main()
