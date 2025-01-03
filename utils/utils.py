import numpy as np


def elucidian_distance(xs: np.ndarray, ys: np.ndarray) -> float:

    assert len(xs) == len(ys), "Input arrays must be the same length"
    distance = np.sqrt(np.sum((ys - xs)**2))

    return distance

def manhattan_distance(xs: np.ndarray, ys: np.ndarray) -> float:

    assert len(xs) == len(ys), "Input arrays must be the same length"
    distance = np.sum(xs - ys)

    return distance


def hamming_distance(s1: str, s2: str) -> int:

    assert len(s1) == len(s2), "Input string must be tha same length"
    distance = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            distance += 1

    return distance
