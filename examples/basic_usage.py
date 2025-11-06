"""
Basic usage examples for addition-subtraction chains.

This example demonstrates the fundamental operations of the library.
"""

import sys
sys.path.insert(0, '..')

import contfrac as cf


def main():
    print("=" * 60)
    print("Basic Addition Chain Generation Examples")
    print("=" * 60)

    # Example 1: Generate chain for n=87 with optimal parameter
    print("\n1. Chain for 87 with optimal parameter:")
    n = 87
    k = cf.alpha(n)
    chain = cf.chain(n, k)
    print(f"   n = {n}")
    print(f"   Optimal k = {k}")
    print(f"   Chain: {chain}")
    print(f"   Chain length: {len(chain)}")

    # Example 2: Using minchain for automatic optimization
    print("\n2. Using minchain for automatic optimization:")
    n = 29
    chain = cf.minchain(n)
    print(f"   n = {n}")
    print(f"   Chain: {chain}")
    print(f"   Chain length: {len(chain)}")

    # Example 3: Power of 2 (optimized)
    print("\n3. Special case - Power of 2:")
    n = 256
    chain = cf.minchain(n)
    print(f"   n = {n}")
    print(f"   Chain: {chain}")
    print(f"   Chain length: {len(chain)}")

    # Example 4: Small number
    print("\n4. Small number:")
    n = 15
    k = cf.alpha(n)
    chain = cf.chain(n, k)
    print(f"   n = {n}")
    print(f"   Optimal k = {k}")
    print(f"   Chain: {chain}")
    print(f"   Chain length: {len(chain)}")

    # Example 5: Larger number
    print("\n5. Larger number:")
    n = 1000
    k = cf.alpha(n)
    chain = cf.chain(n, k)
    print(f"   n = {n}")
    print(f"   Optimal k = {k}")
    print(f"   Chain: {chain}")
    print(f"   Chain length: {len(chain)}")

    # Example 6: Understanding chain operations
    print("\n6. Understanding chain operations:")
    print("   Starting chain: [1, 2, 3]")
    v = [1, 2, 3]

    # Addition operation
    result_add = cf.addition(v.copy(), 2)
    print(f"   After addition(v, 2): {result_add}")

    # Subtraction operation
    result_sub = cf.subtraction([1, 2, 3, 5], 2)
    print(f"   After subtraction([1,2,3,5], 2): {result_sub}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
