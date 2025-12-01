with open("Day1/input1.txt", 'r') as file:
    lines = file.readlines()
    acc = 50
    password = 0
    for line in lines:
        direction = line[0]
        number = int(line[1:].strip())
        if direction == 'R':
            acc += number
        elif direction == 'L':
            acc -= number
        else:
            print("Invalid direction:", direction)
        acc %= 100
        if acc == 0:
            password += 1

    print("Final accumulator value:", acc)
    print("Number of times accumulator returned to zero:", password)
