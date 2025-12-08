
def main(input_lines):
    answer = 0
    ranges = []
    lines = iter(input_lines)
    for line in lines:
        if line.strip() == "":
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    numbers = [int(line) for line in lines]

    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                answer += 1
                break

    return answer


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
