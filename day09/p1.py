import sys


def main() -> None:
    points = open(sys.argv[1]).read().splitlines()
    points = [tuple(map(int, point.split(","))) for point in points]
    n = len(points)
    best = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area

    print(best)


if __name__ == "__main__":
    main()
