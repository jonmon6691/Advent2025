
day6_test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()


def test_day6_part1():
    import d0601
    assert d0601.main(day6_test_input) == 4277556


def test_day6_part2():
    import d0602
    assert d0602.main(day6_test_input) == 3263827
