
dayN_input = """
""".splitlines()

def test_dayN_part1():
    import dNN01
    answer = dNN01.main(dayN_input)
    assert answer == 0

def test_dayN_part2():
    import dNN02
    answer = dNN02.main(dayN_input)
    assert answer == 0
