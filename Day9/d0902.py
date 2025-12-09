from itertools import combinations
from multiprocessing import Process, cpu_count, Queue
from sys import stdout
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inclusive_area(self, other):
        return abs(self.x - other.x + 1) * abs(self.y - other.y + 1)

    def iter_members(self, other):
        for x in range(min(self.x, other.x) + 1, max(self.x, other.x)):
            for y in range(min(self.y, other.y) + 1, max(self.y, other.y)):
                yield Point(x, y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.members = self.compute_members()

    def compute_members(self) -> set[Point]:
        members = set()
        if self.p1.x == self.p2.x:
            x = self.p1.x
            for y in range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y) + 1):
                members.add(Point(x, y))
        elif self.p1.y == self.p2.y:
            y = self.p1.y
            for x in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x) + 1):
                members.add(Point(x, y))
        return members


def main(input_lines):
    pts = [Point(*map(int, line.split(","))) for line in input_lines]
    areas = [(a.inclusive_area(b), a, b) for a, b in combinations(pts, 2)]
    areas.sort(key=lambda x: x[0], reverse=True)

    lines = []
    last_pt = None
    for pt in pts:
        if last_pt is None:
            last_pt = pt
            continue
        lines.append(Line(last_pt, pt))
        last_pt = pt
    lines.append(Line(last_pt, pts[0]))
    lines.sort(key=lambda l: len(l.members), reverse=True)

    for i, (_, a, b) in enumerate(areas):
        print(f"{i}/{len(areas)}", end="")
        for line in lines:  # Largest to smallest, we're looking to fail fast
                failed = False
                print(".", end="")
                sys.stdout.flush()
                for check_point in a.iter_members(b):
                    if check_point in line.members:
                        failed = True
                        break 
                if failed:
                    print()
                    break  # Disproven, go to next biggest area
        else:
            return a.inclusive_area(b)  # No lines disproved, we found it

    return 0  # Should not reach here

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
