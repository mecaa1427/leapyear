from leap import is_leap_year


def test_leap_year():
    assert is_leap_year(2024) == True


def test_non_leap_year():
    assert is_leap_year(2023) == False


def test_century_non_leap():
    assert is_leap_year(1900) == False


def test_century_leap():
    assert is_leap_year(2000) == True


def test_another_leap_year():
    assert is_leap_year(2020) == True