
day1_test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()


def test_part1():
    import d0101
    assert d0101.main(day1_test_input) == 3


def test_part2a():
    import d0102
    assert d0102.main(day1_test_input) == 6
