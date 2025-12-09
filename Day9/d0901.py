from itertools import combinations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inclusive_area(self, other):
        return abs(self.x - other.x + 1) * abs(self.y - other.y + 1)


def main(input_lines):
    pts = [Point(*map(int, line.split(","))) for line in input_lines]
    areas = [a.inclusive_area(b) for a, b in combinations(pts, 2)]
    return max(areas)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
