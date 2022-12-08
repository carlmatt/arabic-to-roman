import pytest

from arabic_to_roman import arabic_number_to_roman_numerals


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "I"),
        (3, "III"),
        (4, "IV"),
        (9, "IX"),
        (56, "LVI"),
        (99, "XCIX"),
        (187, "CLXXXVII"),
        (1234, "MCCXXXIV"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_all_good(number, expected):
    assert arabic_number_to_roman_numerals(number) == expected


@pytest.mark.parametrize(
    "input",
    [(-5), (0), (4000), (99999)],
)
def test_too_small_or_big(input):
    with pytest.raises(ValueError):
        arabic_number_to_roman_numerals(input)


@pytest.mark.parametrize(
    "input",
    [(1.1), (3.14), ("Hello World"), (None)],
)
def test_wrong_type(input):
    with pytest.raises(ValueError):
        arabic_number_to_roman_numerals(input)
