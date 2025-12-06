from itertools import chain
from math import prod

def main(input_lines):
    answer = 0
    nums = []
    op = None
    for col in chain(zip(*input_lines), [' ']): # Rotate and add extra blank row
        num = ''.join(col[:-1]).strip()
        op_char = col[-1].strip()
        if not num: # Blank column indicates end of current equation
            if not op: raise ValueError("No operator found for column")
            if op == "+": answer += sum(nums)
            elif op == "*": answer += prod(nums)
            else: raise ValueError(f"Unknown operator: {op}")
            nums = []
            op = None
            continue
        if op_char:
            if op: raise ValueError("Multiple operators found for column")
            op = col[-1]
        nums.append(int(num))
    return answer

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        print(f"Answer: {main(f.read().splitlines())}")
