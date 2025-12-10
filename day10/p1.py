import sys
import re
from collections import deque


def main() -> None:
    manual = open(sys.argv[1]).read().splitlines()
    total = 0

    for line in manual:
        diagram = re.search(r'\[([.#]+)\]', line)
        pattern = diagram.group(1) if diagram else ''
        n = len(pattern)

        target_mask = 0
        for i, ch in enumerate(pattern):
            if ch == '#':
                target_mask |= 1 << i

        button_groups = re.findall(r'\(([^)]*)\)', line)
        button_masks = []

        for buttons in button_groups:
            mask = 0
            for button in map(int, buttons.split(',')):
                mask |= 1 << button
            button_masks.append(mask)

        def fewest_presses_bfs() -> int:
            dist = [-1] * (1 << n)
            dist[0] = 0
            q = deque([0])

            while q:
                cur_state = q.popleft()
                cur_dist = dist[cur_state]

                for button_mask in button_masks:
                    next_state = cur_state ^ button_mask
                    if dist[next_state] == -1:
                        dist[next_state] = cur_dist + 1
                        if next_state == target_mask:
                            return dist[next_state]
                        q.append(next_state)

            raise ValueError("Target state is unreachable")

        total += fewest_presses_bfs()

    print(total)


if __name__ == "__main__":
    main()
