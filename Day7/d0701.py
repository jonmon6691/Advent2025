
def main(input_lines):
    answer = 0
    beam_ids = set()
    for line in input_lines:
        next_row = beam_ids.copy()
        next_row.add(line.find('S'))
        for i, c in enumerate(line):
            if c == '^':
                if i in beam_ids:
                    next_row.add(i - 1)
                    next_row.remove(i)
                    next_row.add(i + 1)
                    answer += 1
        beam_ids = next_row
    return answer

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
