"""Exercise 03: dictionary"""

__author__: str = "730655640"


def invert(d: dict[str, str]) -> dict[str, str]:
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError("Duplicate values found, cannot invert dictionary!")
        inverted[value] = key
    return inverted


def count(values: list[str]) -> dict[str, int]:
    """counts the occurences of each unique string in the given list."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """returns the most frequently occurring color from the given dictionary."""
    color_counts = count(list(colors.values()))
    max_count = max(color_counts.values())
    for color in colors.values():
        if color_counts[color] == max_count:
            return color
    return "all done"


def bin_len(words: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
    return bins
