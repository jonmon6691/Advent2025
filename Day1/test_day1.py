
day1_test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def test_part1():
    import d0101
    lines = day1_test_data.splitlines()
    password = d0101.main(lines)
    assert password == 3

day2_test_data = day1_test_data

def test_part2a():
    import d0102
    lines = day2_test_data.splitlines()
    password = d0102.main(lines)
    assert password == 6
