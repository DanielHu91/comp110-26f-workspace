"""Write at least two expected-case tests and one edge-case test per function."""

__author__: str = "730664641"


# Uncomment this import and example when you are ready to test scale_range.
import pytest

from daftcomp import HOLD, REST
from list_utils.utils import caesar, halftime, reverse, scale_range, shift_mutate, shift_pure


def test_scale_range_ascending() -> None:
    """An ascending range includes values before the stop."""
    assert scale_range(1, 10, 2) == [1, 3, 5, 7, 9]


def test_scale_range_positive_step() -> None:
    """A positive step produces consecutive values."""
    assert scale_range(2, 8, 1) == [2, 3, 4, 5, 6, 7]


def test_scale_range_zero_step() -> None:
    """A zero step raises an AssertionError."""
    with pytest.raises(AssertionError):
        scale_range(1, 10, 0)


def test_shift_mutate_positive() -> None:
    """Tests a positive shift."""
    original: list[int] = [60, 64, 67]
    result = shift_mutate(original, 12)

    assert original == [72, 76, 79]
    assert result is None


def test_shift_mutate_negative() -> None:
    """Tests a negative shift."""
    original: list[int] = [60, 64, 67]
    shift_mutate(original, -12)

    assert original == [48, 52, 55]


def test_shift_mutate_alias() -> None:
    """Tests a shift with an alias."""
    original: list[int] = [60, 64]
    alias: list[int] = original

    shift_mutate(original, 12)

    assert alias == [72, 76]
    assert alias is original


def test_shift_mutate_empty() -> None:
    """Shifting an empty list leaves it empty."""
    original: list[int] = []
    result = shift_mutate(original, 12)

    assert original == []
    assert result is None


def test_shift_pure_positive() -> None:
    """Tests a positive shift."""
    original: list[int] = [60, 64, 67]
    result: list[int] = shift_pure(original, 12)

    assert original == [60, 64, 67]
    assert result == [72, 76, 79]
    assert result is not original


def test_shift_pure_negative() -> None:
    """Tests a negative shift."""
    original: list[int] = [60, 64, 67]
    result: list[int] = shift_pure(original, -12)

    assert original == [60, 64, 67]
    assert result == [48, 52, 55]
    assert result is not original


def test_shift_pure_empty() -> None:
    """Tests an empty list."""
    original: list[int] = []
    result: list[int] = shift_pure(original, 12)

    assert original == []
    assert result == []
    assert result is not original


def test_reverse_list() -> None:
    """Tests a normal list with three integers."""
    original: list[int] = [60, 64, 67]
    result: list[int] = reverse(original)

    assert result == [67, 64, 60]
    assert original == [60, 64, 67]
    assert original is not result


def test_reverse_repeat() -> None:
    """Tests a list with repeated integers."""
    original: list[int] = [60, 60, 64, 67]
    result: list[int] = reverse(original)

    assert original == [60, 60, 64, 67]
    assert result == [67, 64, 60, 60]
    assert result is not original


def test_reverse_empty() -> None:
    """Tests an empty list."""
    original: list[int] = []
    result: list[int] = reverse(original)

    assert result == []
    assert original == []
    assert result is not original


def test_halftime_notes() -> None:
    """Tests a normal list."""
    original: list[int] = [60, 64]
    result: list[int] = halftime(original)

    assert original == [60, 64]
    assert result == [60, HOLD, 64, HOLD]


def test_halftime_rest() -> None:
    """Tests a list with rest."""
    original: list[int] = [60, REST, 64]
    result: list[int] = halftime(original)

    assert original == [60, REST, 64]
    assert result == [60, HOLD, REST, REST, 64, HOLD]


def test_halftime_empty() -> None:
    """Tests an empty list."""
    original: list[int] = []
    result: list[int] = halftime(original)

    assert original == []
    assert result == []


def test_caesar_wraparound() -> None:
    """Tests a normal list."""
    original: list[int] = [0, 1, 3, 64, 127]
    result: list[int] = caesar(original)

    assert original == [0, 1, 3, 64, 127]
    assert result == [64, 65, 67, 0, 63]


def test_caesar_special() -> None:
    """Tests a list with hold and rest."""
    original: list[int] = [60, HOLD, REST, 67]
    result: list[int] = caesar(original)

    assert original == [60, HOLD, REST, 67]
    assert result == [124, HOLD, REST, 3]


def test_caesar_empty() -> None:
    """Tests an empty list."""
    original: list[int] = []
    result: list[int] = caesar(original)

    assert original == []
    assert result == []


# Add your tests here. The supplied example does not count toward your 18 tests.
# Test values, unchanged inputs and fresh lists, or mutation through an alias.
