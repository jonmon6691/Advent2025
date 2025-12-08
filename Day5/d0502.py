class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.start <= other.end and other.start <= self.end

    def merge(self, other):
        return Range(min(self.start, other.start), max(self.end, other.end))

    def length(self):
        return self.end - self.start + 1


def main(input_lines):
    ranges = []
    for line in input_lines:
        if line.strip() == "":
            break
        start, end = map(int, line.split("-"))
        ranges.append(Range(start, end))

    ranges = sorted(ranges, key=lambda x: x.start)
    merged_ranges = []
    for r in ranges:
        if not merged_ranges or not merged_ranges[-1].overlaps(r):
            merged_ranges.append(r)
        else:
            merged_ranges[-1] = merged_ranges[-1].merge(r)

    return sum(r.length() for r in merged_ranges)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
