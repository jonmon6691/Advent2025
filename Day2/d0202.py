# Doing it the
import re#gexy way

def main(ranges_str):
    acc = 0
    for range_str in ranges_str.split(','):
        start, end = map(int, range_str.split('-'))
        for i in range(start, end + 1):
            if re.match(r'^(\d+)\1+$', str(i)):
                acc += i
    return acc

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print(f"Answer: {main(lines.pop())}")
