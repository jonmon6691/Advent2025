from collections import defaultdict


def main(input_lines):
    beam_ids = defaultdict(int)
    for line in input_lines:
        next_row = beam_ids.copy()
        start_id = line.find('S')
        if start_id != -1:
            next_row[start_id] += 1
        for i, c in enumerate(line):
            if c == '^':
                if i in beam_ids:
                    next_row[i - 1] += beam_ids[i]
                    next_row.pop(i)
                    next_row[i + 1] += beam_ids[i]
        beam_ids = next_row
    return sum(beam_ids.values())


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
