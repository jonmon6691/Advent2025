
day5_test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

def test_day5_part1():
    import d0501
    assert d0501.main(day5_test_input) == 3

def test_day5_part2():
    import d0502
    assert d0502.main(day5_test_input) == 14
