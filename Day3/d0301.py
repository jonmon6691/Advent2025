
def main(input_lines):
    answer = 0
    for line in input_lines:
        js = [int(c) for c in line.strip()]
        first_digit = max(js[:-1])
        second_digit = max(js[js.index(first_digit)+1:])
        answer += first_digit * 10 + second_digit
    return answer


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
    print(f"Answer: {main(lines)}")
