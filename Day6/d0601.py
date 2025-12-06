from math import prod
def main(input_lines):
    rows = []
    answer = 0
    for line in input_lines:
        rows.append([n for n in line.split()])
    for equation in zip(*rows):
        nums, op = equation[:-1], equation[-1]
        nums = list(map(int, nums))
        if op == "+": answer += sum(nums)
        elif op == "*": answer += prod(nums)
        else: raise ValueError(f"Unknown operator: {op}")
    return answer

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
