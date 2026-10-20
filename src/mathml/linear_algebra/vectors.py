"""Vector operations implemented using pure Python."""

from math import sqrt


def add_vectors(a, b):
    """Return the component-wise sum of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    return [x + y for x, y in zip(a, b)]


def subtract_vectors(a, b):
    """Return the component-wise difference of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    return [x - y for x, y in zip(a, b)]


def scale_vector(scalar, vector):
    """Multiply every component by a scalar."""
    return [scalar * x for x in vector]


def dot_product(a, b):
    """Return the dot product of two vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    return sum(x * y for x, y in zip(a, b))


def magnitude(vector):
    """Return the Euclidean magnitude of a non-empty vector."""
    if len(vector) == 0:
        raise ValueError("Vector must contain at least one component.")

    return sqrt(sum(x ** 2 for x in vector))


def cosine_similarity(a, b):
    """Return cosine similarity for two non-zero vectors."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")

    magnitude_a = magnitude(a)
    magnitude_b = magnitude(b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")

    return dot_product(a, b) / (magnitude_a * magnitude_b)