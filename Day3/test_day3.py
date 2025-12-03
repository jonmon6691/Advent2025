
day3_test_input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

def test_day3_part1():
    import d0301
    assert d0301.main(day3_test_input) == 357

def test_day3_part2():
    import d0302
    assert d0302.main(day3_test_input) == 3121910778619
