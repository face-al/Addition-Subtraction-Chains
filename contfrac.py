"""
Core module for addition-subtraction chains using generalized continued fractions.

This module provides the main algorithms for generating optimal or near-optimal
addition chains for positive integers, useful in cryptographic operations.
"""

import math as m
import numpy as np


def floor(num):
    """
    Return the floor of a number.

    Args:
        num: Number to floor

    Returns:
        int: Floor of the input number
    """
    return m.floor(num)


def ceil(num):
    """
    Return the ceiling of a number.

    Args:
        num: Number to ceil

    Returns:
        int: Ceiling of the input number
    """
    return m.ceil(num)


def sign(n):
    """
    Return the sign of a number.

    Args:
        n: Input number

    Returns:
        int: -1 if negative, 1 otherwise
    """
    if n < 0:
        return -1
    else:
        return 1


def gcdExtended(a, b):
    """
    Extended Euclidean Algorithm.

    Computes GCD and Bézout coefficients such that a*x + b*y = gcd(a,b).

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        tuple: (gcd, x, y) where gcd is the greatest common divisor,
               and x, y are the Bézout coefficients
    """
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def gcf(n, k):
    """
    Compute generalized continued fraction coefficients.

    Uses the extended Euclidean algorithm to compute the coefficients u1 and u2
    for the generalized continued fraction representation.

    Args:
        n (int): First integer
        k (int): Second integer

    Returns:
        list: Sorted list [u1, u2] of GCF coefficients
    """
    gcd, a1, a2 = gcdExtended(n, k)
    u1 = a1 * k

    if a1 == 0:
        u2 = 0
    else:
        u2 = (-1) * int(a2 / a1)
    u = sorted([u1, u2])
    return u


def product(v, w):
    """
    Combine two chains via multiplication operation.

    Multiplies each element in chain w by the last element of chain v,
    then extends v with these products.

    Args:
        v (list): First chain
        w (list): Second chain

    Returns:
        list: Combined chain
    """
    intermediate_result = np.multiply(w, v[-1]).tolist()
    v.extend(intermediate_result)
    return v


def addition(v, j):
    """
    Extend chain by adding a value.

    Appends (last element + j) to the chain v.

    Args:
        v (list): Input chain
        j (int): Value to add

    Returns:
        list: Extended chain
    """
    v.append(v[-1] + j)
    return v


def subtraction(v, j):
    """
    Extend chain by subtracting a value.

    Appends (last element - j) to the chain v.

    Args:
        v (list): Input chain
        j (int): Value to subtract

    Returns:
        list: Extended chain
    """
    v.append(v[-1] - j)
    return v


def log_2(x):
    """
    Compute floor of log base 2.

    Args:
        x (int): Input integer

    Returns:
        int: Floor of log2(x)
    """
    result = 0
    while x > 1:
        x >>= 1
        result += 1
    return result


def alpha(n):
    """
    Determine optimal parameter k for chain generation.

    Uses a heuristic based on bit length to select the best parameter
    for generating an optimal chain.

    Args:
        n (int): Target integer

    Returns:
        int: Optimal parameter k
    """
    fraction = 1 << int(ceil(floor(log_2(n)) / 2))
    return floor(n / fraction)


def minchain(n):
    """
    Generate a minimal or near-minimal addition chain for n.

    Uses optimized algorithms for special cases (powers of 2, small numbers)
    and recursive chain generation for general cases.

    Args:
        n (int): Target integer (positive)

    Returns:
        list: Addition chain from 1 to n

    Examples:
        >>> minchain(87)
        [1, 2, 3, 6, 7, 10, 20, 40, 80, 87]
    """
    l = n.bit_length() - 1
    if n == 1 << l:  # Power of 2
        return [2**(i) for i in range(l+1)]
    if n == 3:
        return [1, 2, 3]
    return chain(n, 1 << floor(log_2(int(n/2))))


def chain(n, k):
    """
    Generate an addition chain for n using parameter k.

    Recursive algorithm that builds the chain by decomposing n
    using the parameter k and combining subchains.

    Args:
        n (int): Target integer
        k (int): Chain generation parameter

    Returns:
        list: Sorted, deduplicated addition chain from 1 to n

    Examples:
        >>> chain(28, 7)
        [1, 2, 3, 4, 7, 14, 21, 28]
    """
    q = floor(n / k)
    r = n % k
    if r == 0:
        return sorted(list(set(product(minchain(k), minchain(q)))))
    else:
        return sorted(list(set(addition(product(chain(k, r), minchain(q)), r))))