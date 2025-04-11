"""Exercise 03: Tests"""

__author__: str = "730655640"

from dictionary import invert, count, favorite_color, bin_len
import pytest

# test of invert


def test_invert_1() -> None:
    # test that a simple dictionary is correctly inverted
    assert invert({"a": "d", "b": "e", "c": "f"}) == {"d": "a", "e": "b", "f": "c"}


def test_invert_2() -> None:
    # test that a single key-value pair is correctly inverted
    assert invert({"pie": "apple", "butter": "peanut"}) == {
        "apple": "pie",
        "peanut": "butter",
    }


def test_invert_3() -> None:
    # test that a dictionary with duplicate values raises a KeyError
    with pytest.raises(KeyError):
        my_dictionary = {"apple": "pie", "pumpkin": "pie"}
        invert(my_dictionary)


# Tests of count


def test_count_1() -> None:
    # test that a list with repeated values returns correct counts
    assert count(["apple", "banana", "apple", "cherry", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "cherry": 1,
    }


def test_count_2() -> None:
    # test that a list with a single value retunrs count of 1
    assert count(["grape"]) == {"grape": 1}


def test_count_3() -> None:
    # test that an empty list retunrs an empty dictionary
    assert count([]) == {}


# Tests of favorite_color


def test_favorite_color_1() -> None:
    # test that the most frequently occurring color is returned
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_2() -> None:
    # test that in case of a tie, the first encountered color is returned
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "red", "Charlie": "red", "David": "blue"}
        )
        == "blue"
    )


def test_favorite_color_3() -> None:
    # test that if only one person is present, their favorite color it returned
    assert favorite_color({"Alice": "green"}) == "green"


# tests of bin_len


def test_bin_len_1() -> None:
    # test that words are correctly grouped by length
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_2() -> None:
    # test that duplicate words do not create duplicate entries in sets
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_3() -> None:
    # test that an empty list returns an empty dictionary
    assert bin_len([]) == {}
