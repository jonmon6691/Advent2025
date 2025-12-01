with open("Day1/input1.txt", 'r') as file:
    lines = file.readlines()
    acc = 50
    password = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:].strip())
        if direction == 'R':
            while number > 0:
                number -= 1
                acc += 1
                acc %= 100
                if acc == 0:
                    password += 1
        elif direction == 'L':
            while number > 0:
                number -= 1
                acc -= 1
                acc %= 100
                if acc == 0:
                    password += 1
        else:
            print("Invalid direction:", direction)

    print("Final accumulator value:", acc)
    print("Number of times accumulator returned to zero:", password)
