import sys


def main() -> None:
    red_tiles = open(sys.argv[1]).read().splitlines()
    red_tiles = [tuple(map(int, red_tile.split(","))) for red_tile in red_tiles]
    n = len(red_tiles)

    horizontal_edges = []
    vertical_edges = []

    for i in range(n):
        (x1, y1), (x2, y2) = red_tiles[i], red_tiles[(i + 1) % n]

        if x1 == x2:
            if y1 < y2:
                vertical_edges.append((x1, y1, y2))
            else:
                vertical_edges.append((x1, y2, y1))
        elif y1 == y2:
            if x1 < x2:
                horizontal_edges.append((y1, x1, x2))
            else:
                horizontal_edges.append((y1, x2, x1))
        else:
            raise ValueError("Edges must be axis-aligned")

    def cross_boundary(x1, x2, y1, y2) -> bool:
        for y, ax, bx in horizontal_edges:
            if not y1 < y < y2:
                continue
            lo = max(x1, ax)
            hi = min(x2, bx)
            if hi > lo:
                return True

        for x, ay, by in vertical_edges:
            if not x1 < x < x2:
                continue
            lo = max(y1, ay)
            hi = min(y2, by)
            if hi > lo:
                return True

        return False

    def point_on_segment(px, py, x1, y1, x2, y2) -> bool:
        if x1 == x2:
            if px != x1:
                return False
            return min(y1, y2) <= py <= max(y1, y2)
        if y1 == y2:
            if py != y1:
                return False
            return min(x1, x2) <= px <= max(x1, x2)
        return False

    def point_in_polygon(px, py) -> bool:
        for i in range(n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[(i + 1) % n]
            if point_on_segment(px, py, x1, y1, x2, y2):
                return True

        inside = False

        for i in range(n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[(i + 1) % n]

            if y1 == y2:
                continue

            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            if not (y1 <= py < y2):
                continue

            if x1 > px:
                inside = not inside

        return inside

    best = 0

    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]

            xa, xb = sorted((x1, x2))
            ya, yb = sorted((y1, y2))

            area = (xb - xa + 1) * (yb - ya + 1)
            if area <= best:
                continue

            if cross_boundary(xa, xb, ya, yb):
                continue

            cx = (xa + xb) / 2
            cy = (ya + yb) / 2
            if not point_in_polygon(cx, cy):
                continue

            best = area

    print(best)


if __name__ == "__main__":
    main()
