
def test_part_2_check_valid_id():
    from part2 import check_valid_id

    assert check_valid_id(11) is False
    assert check_valid_id(22) is False
    assert check_valid_id(999) is False
    assert check_valid_id(1010) is False
    assert check_valid_id(446446) is False
    assert check_valid_id(824824824) is False
    assert check_valid_id(2121212121) is False

    assert check_valid_id(10) is True
    assert check_valid_id(21) is True
    assert check_valid_id(998) is True
    assert check_valid_id(1012) is True
    assert check_valid_id(446447) is True
    assert check_valid_id(824824825) is True
    assert check_valid_id(2121212122) is True

test_part_2_check_valid_id()