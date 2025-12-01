def main(lines):
    acc = 50
    password = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:].strip())
        
        password += number // 100
        number %= 100

        for _ in range(number):
            acc += 1 if direction == 'R' else -1
            acc %= 100
            if acc == 0:
                password += 1

    return password

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        print(f"Password = {main(lines)}")
