
day3_input = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

def test_day3_part1():
    import d0301
    answer = d0301.main(day3_input)
    assert answer == 357

def test_day3_part2():
    import d0302
    answer = d0302.main(day3_input)
    assert answer == 3121910778619
