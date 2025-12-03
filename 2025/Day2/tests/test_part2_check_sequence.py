
def test_part_2_check_sequence():
    from part2 import check_sequence

    assert check_sequence("2121212122", 2) is True
    assert check_sequence("2121212122", 3) is True
    assert check_sequence("2121212122", 4) is True
    assert check_sequence("2121212122", 5) is True
    assert check_sequence("2121212122", 10) is True
    assert check_sequence("11", 1) is False
    assert check_sequence("11", 2) is True
    assert check_sequence("12", 1) is True
    assert check_sequence("12", 2) is True
    assert check_sequence("2121212121", 2) is False
    assert check_sequence("2121212122", 2) is True
    assert check_sequence("446446", 3) is False
    assert check_sequence("1111", 1) is False
    assert check_sequence("12", 1) is True
    assert check_sequence("1212", 2) is False
    assert check_sequence("123123", 3) is False
    assert check_sequence("12341234", 4) is False
    assert check_sequence("123123123", 3) is False
    assert check_sequence("123456", 3) is True
    assert check_sequence("111222", 3) is True

test_part_2_check_sequence()