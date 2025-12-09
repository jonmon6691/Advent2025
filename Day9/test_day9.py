
day9_test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".splitlines()


def test_day9_part1():
    import d0901
    assert d0901.main(day9_test_input) == 50


def test_day9_part2():
    import d0902
    assert d0902.main(day9_test_input) == 24
