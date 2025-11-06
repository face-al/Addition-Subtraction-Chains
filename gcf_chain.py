"""
Enhanced GCF-based addition chain module with multiple strategies.

This module provides chain generation with support for different parameter
selection strategies: Binary, Square-root, Factor, Pi, Golden-ratio, etc.
"""

import contfrac as cf
import math as m


# Strategy Reference:
# 1: Binary Strategy (floor(n/2))
# 2: Square-root Strategy (floor(sqrt(n)))
# 3: Factor Strategy
# 4: Pi Strategy
# 5: Golden-Ratio Strategy
# 6: Square-root Strategy
# 7: Seventh Strategy
# 8: Ones strategy


def minchain(n, strategy_num):
    """
    Generate minimal chain using specified strategy.

    Provides multiple strategies for selecting the parameter k,
    which affects chain generation performance.

    Args:
        n (int): Target integer
        strategy_num (int): Strategy selection:
            1 = Binary Strategy (floor(n/2))
            2 = Square-root Strategy (floor(sqrt(n)))

    Returns:
        list: Addition chain from 1 to n

    Examples:
        >>> minchain(63, strategy_num=1)  # Binary strategy
        [1, 2, 4, 8, 16, 31, 32, 63]
    """
    l = n.bit_length() - 1
    strategy = {1: cf.floor(n/2), 2: cf.floor(m.sqrt(n))}

    # Special case: power of 2
    if n == 1 << l:
        return [2**(i) for i in range(l+1)]

    # Special case: 3
    if n == 3:
        return [1, 2, 3]

    k = strategy[strategy_num]
    return chain(n, k, strategy_num)


def chain(n, k, strategy_num):
    """
    Generate addition chain using GCF with specified strategy.

    Uses generalized continued fraction coefficients to build the chain
    recursively with addition/subtraction operations.

    Args:
        n (int): Target integer
        k (int): Chain generation parameter
        strategy_num (int): Strategy number for recursive calls

    Returns:
        list: Sorted, deduplicated addition chain from 1 to n

    Examples:
        >>> chain(63, 7, 1)
        [1, 2, 3, 4, 7, 14, 21, 28, 56, 63]
    """
    u = cf.gcf(n, k)

    # Check if u1 and u2 are not 0
    if u[0] == 0 or u[1] == 0:
        return cf.chain(n, k)

    q0 = m.gcd(n, k)
    q1 = abs(u[0]) * q0

    x0 = minchain(abs(q0), strategy_num)
    x1 = cf.product(x0, minchain(abs(u[0]), strategy_num))
    x2 = cf.product(x1, minchain(abs(u[1]), strategy_num))

    # Apply addition or subtraction based on sign of u[0]
    if u[0] < 0:
        x2 = cf.subtraction(x2, q0)
    else:
        x2 = cf.addition(x2, q0)

    return sorted(list(set(x2)))


if __name__ == "__main__":
    # Example usage
    k = 3
    result = chain(63, 7, 1)
    print(f"Chain for 63: {result}")





