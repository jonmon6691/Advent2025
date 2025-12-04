
day4_test_input = \
"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

def test_day4_part1():
    import d0401
    assert d0401.main(day4_test_input) == 13

def test_day4_part2():
    import d0402
    assert d0402.main(day4_test_input) == 43
