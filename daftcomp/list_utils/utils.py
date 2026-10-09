"""Implement the six list functions described in README.md using while loops."""

__author__: str = "730664641"

from daftcomp import HOLD, REST


def scale_range(start: int, stop: int, step: int) -> list[int]:
    """Build a range with an exclusive stop; assert that step is nonzero."""

    assert step != 0

    result: list[int] = []
    current: int = start

    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    else:
        while current > stop:
            result.append(current)
            current += step

    return result

    raise NotImplementedError("Build a new list using a while loop and append.")


def shift_mutate(original: list[int], offset: int) -> None:
    """Add offset to EVERY integer in the caller's list; return None."""

    index: int = 0

    while index < len(original):
        original[index] = original[index] + offset
        index += 1


def shift_pure(original: list[int], offset: int) -> list[int]:
    """Return a new list with offset added to EVERY integer; preserve original."""

    index: int = 0
    new: list[int] = []

    while index < len(original):
        new.append(original[index] + offset)
        index += 1

    return new
    raise NotImplementedError("Build an independent list of shifted integers.")


def reverse(original: list[int]) -> list[int]:
    """Return the integers in reverse order in a new list; preserve original."""

    index: int = 1
    result: list[int] = []

    while index < len(original) + 1:
        result.append(original[len(original) - index])
        index += 1

    return result

    raise NotImplementedError("Start at the final index and work backward.")


def halftime(original: list[int]) -> list[int]:
    """Return a new list with each step extended to twice its duration."""

    index: int = 0
    result: list[int] = []

    while index < len(original):
        result.append(original[index])

        if original[index] == REST:
            result.append(REST)
        else:
            result.append(HOLD)

        index += 1

    return result

    raise NotImplementedError("Append each original entry, then an extra HOLD or REST.")


def caesar(original: list[int]) -> list[int]:
    """Rotate values 0..127 by 64, preserving REST/HOLD, in a new list."""

    index: int = 0
    result: list[int] = []

    while index < len(original):
        value = original[index] + 64
        if original[index] == REST or original[index] == HOLD:
            result.append(original[index])
        elif value > 127:
            result.append(value - 128)
        else:
            result.append(value)

        index += 1

    return result

    raise NotImplementedError("Wrap shifted values using the remainder operator.")
