# Doing it the
import math#y way


def main(ranges_str):
    acc = 0
    for range_str in ranges_str.split(','):
        start, end = map(int, range_str.split('-'))
        for i in range(start, end + 1):
            num_digits = math.floor(math.log10(i)) + 1
            if num_digits % 2 == 1:
                continue  # Skip numbers with odd number of digits
            top_half = i // (10 ** (num_digits // 2))
            bottom_half = i % (10 ** (num_digits // 2))
            if top_half == bottom_half:
                acc += i
    return acc


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print(f"Answer: {main(lines.pop())}")
