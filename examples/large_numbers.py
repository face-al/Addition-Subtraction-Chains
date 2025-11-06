"""
Working with large numbers for cryptographic applications.

This example demonstrates chain generation for large integers
typical in cryptographic operations like elliptic curve cryptography.
"""

import sys
sys.path.insert(0, '..')

import contfrac as cf
import time


def benchmark_chain_generation(n, description):
    """Generate chain and benchmark performance."""
    print(f"\n{description}")
    print(f"Number: {n}")
    print(f"Bit length: {n.bit_length()}")

    start_time = time.time()
    k = cf.alpha(n)
    chain = cf.chain(n, k)
    elapsed = time.time() - start_time

    print(f"Parameter k: {k}")
    print(f"Chain length: {len(chain)}")
    print(f"Time elapsed: {elapsed:.6f} seconds")
    print(f"Efficiency (log2(n)): {n.bit_length()}")
    print(f"Actual chain length: {len(chain)}")
    print(f"Ratio (chain/log2(n)): {len(chain) / n.bit_length():.2f}")

    return chain


def main():
    print("=" * 70)
    print("Addition Chains for Cryptographic-Sized Numbers")
    print("=" * 70)

    # Example 1: 32-bit number
    n1 = 2**32 - 1  # Max 32-bit unsigned
    benchmark_chain_generation(n1, "Example 1: 32-bit number (2^32 - 1)")

    # Example 2: 64-bit number
    n2 = 2**64 - 1  # Max 64-bit unsigned
    benchmark_chain_generation(n2, "Example 2: 64-bit number (2^64 - 1)")

    # Example 3: 128-bit number (common in cryptography)
    n3 = 2**127 - 1  # Mersenne prime
    benchmark_chain_generation(n3, "Example 3: 128-bit Mersenne prime (2^127 - 1)")

    # Example 4: 256-bit number (common in ECC)
    n4 = 2**256 - 2**32 - 977  # secp256k1 order (Bitcoin curve) - approximation
    benchmark_chain_generation(n4, "Example 4: 256-bit number (similar to secp256k1)")

    # Example 5: Custom large number from test suite
    n5 = 26235947428953663183191
    benchmark_chain_generation(n5, "Example 5: 70-bit custom number")

    print("\n" + "=" * 70)
    print("\nPerformance Notes:")
    print("  - Chain length typically grows as O(log n)")
    print("  - For cryptographic operations, shorter chains = faster computation")
    print("  - Powers of 2 have optimal chains of exactly log2(n) + 1 elements")
    print("=" * 70)


if __name__ == "__main__":
    main()
