"""
Bos-Coster algorithm implementation using Non-Adjacent Form (NAF).

This module provides utilities for converting integers to NAF representation
and implements the Bos-Coster algorithm for efficient multi-exponentiation.

NAF is useful for reducing the number of non-zero digits in binary
representations, which is valuable for cryptographic operations.
"""

import numpy as np


def NAF(x):
    """
    Convert an integer to Non-Adjacent Form (NAF).

    NAF is a signed binary representation where no two adjacent digits are non-zero.
    This representation minimizes the number of non-zero digits, which is useful
    for efficient exponentiation algorithms.

    Args:
        x (int): Input integer (signed)

    Returns:
        list: NAF representation with elements in {-1, 0, 1}
              Represented as list where -1 can appear

    Examples:
        >>> NAF(13)
        [1, 0, -1, 0, 1]
        # This represents: 16 - 4 + 1 = 13

    Notes:
        - For signed integers only
        - For unsigned integers, slight modification needed
    """
    if x == 0:
        return []
    z = 0 if x % 2 == 0 else 2 - (x % 4)
    return NAF((x - z) // 2) + [z]


# TODO: Implement NAF_inverse function to convert NAF back to integer


def compute_naf_statistics(n):
    """
    Compute statistics about NAF representation.

    Args:
        n (int): Input integer

    Returns:
        dict: Dictionary with NAF statistics including:
            - naf: NAF representation
            - zeros: Number of zeros
            - length: Total length
            - p: Probability of zero (zeros/length)
            - q_1: Probability of non-zero (for signed NAF)
    """
    n_naf = NAF(n)
    zeros_in_n = n_naf.count(0)
    l = len(n_naf)

    # p = # of 0's / length of n (bit length)
    p = zeros_in_n / l

    # q_1 because we are dealing with NAF (signed integer)
    q_1 = round((1 - p) / 2, 2)

    return {
        'naf': n_naf,
        'zeros': zeros_in_n,
        'length': l,
        'p': p,
        'q_1': q_1
    }


if __name__ == "__main__":
    # Example usage as in Doche 9.35
    n = 587257

    stats = compute_naf_statistics(n)
    print(f"NAF of {n}: {stats['naf']}")
    print(f"Zeros: {stats['zeros']}, Length: {stats['length']}")
    print(f"Probability p: {stats['p']:.3f}, q_1: {stats['q_1']:.3f}")

    # Bos-Coster tree structure (partial implementation)
    # k = 4 as in 9.35 from Doche
    # leaves are initially 1, just the root initially
    k = 4
    tree = {"root": 1}
    signed_appending = {stats['p']: 0, stats['q_1']: [-10, 10]}
    tree.update(signed_appending)
    print(f"Tree structure: {tree}")
