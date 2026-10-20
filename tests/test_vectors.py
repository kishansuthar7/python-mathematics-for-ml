"""Tests for the reusable vector operations."""

import numpy as np
import pytest

from mathml.linear_algebra.vectors import (
    add_vectors,
    cosine_similarity,
    dot_product,
    magnitude,
    scale_vector,
    subtract_vectors,
)


def test_add_vectors() -> None:
    assert add_vectors([2, 3], [1, 4]) == [3.0, 7.0]


def test_subtract_vectors() -> None:
    assert subtract_vectors([2, 3], [1, 4]) == [1.0, -1.0]


def test_scale_vector() -> None:
    assert scale_vector(3, [2, 3]) == [6.0, 9.0]


def test_dot_product() -> None:
    assert dot_product([2, 3], [1, 4]) == pytest.approx(14.0)


def test_magnitude() -> None:
    assert magnitude([2, 3]) == pytest.approx(np.sqrt(13))


def test_cosine_similarity() -> None:
    expected = 14 / (np.sqrt(13) * np.sqrt(17))
    assert cosine_similarity([2, 3], [1, 4]) == pytest.approx(expected)


def test_accepts_numpy_arrays() -> None:
    result = add_vectors(np.array([2, 3]), np.array([1, 4]))
    assert result == [3.0, 7.0]


def test_rejects_mismatched_dimensions() -> None:
    with pytest.raises(ValueError, match="same dimension"):
        add_vectors([1, 2], [3])


def test_rejects_empty_vectors() -> None:
    with pytest.raises(ValueError, match="at least one component"):
        magnitude([])


def test_cosine_similarity_rejects_zero_vector() -> None:
    with pytest.raises(ValueError, match="zero vector"):
        cosine_similarity([0, 0], [1, 2])
