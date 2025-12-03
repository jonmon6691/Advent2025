
def main(input_lines):
    answer = 0
    for line in input_lines:
        js = [int(c) for c in line.strip()]
        bignum = recurse_me_baby(js, 12)
        bignum = int("".join([str(d) for d in bignum]))
        answer += bignum
    return answer

def recurse_me_baby(js, len):
    if len == 1:
        return [max(js)]
    
    max_digit = max(js[:1-len])
    return [max_digit] + recurse_me_baby(js[js.index(max_digit)+1:], len - 1)

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    print(f"Answer: {main(lines)}")
