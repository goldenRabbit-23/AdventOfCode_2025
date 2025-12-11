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

        total = 0

        for neigh in graph[current]:
            total += dfs(neigh, target)

        return total

    # Scenario 1: svr -> dac -> fft -> out
    s1_part1 = dfs("svr", "dac")
    s1_part2 = dfs("dac", "fft")
    s1_part3 = dfs("fft", "out")
    scenario1 = s1_part1 * s1_part2 * s1_part3

    # Scenario 2: svr -> fft -> dac -> out
    s2_part1 = dfs("svr", "fft")
    s2_part2 = dfs("fft", "dac")
    s2_part3 = dfs("dac", "out")
    scenario2 = s2_part1 * s2_part2 * s2_part3

    print(scenario1 + scenario2)


if __name__ == "__main__":
    main()
