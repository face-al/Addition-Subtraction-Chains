"""
Non-Adjacent Form (NAF) usage examples.

This example demonstrates NAF conversion and its applications
in cryptographic operations.
"""

import sys
sys.path.insert(0, '..')

import bos_coster as bc


def print_naf_analysis(n):
    """Print detailed NAF analysis for a number."""
    print(f"\nNumber: {n}")
    print(f"Binary: {bin(n)}")

    naf = bc.NAF(n)
    print(f"NAF: {naf}")

    # Count non-zero elements
    non_zeros = sum(1 for x in naf if x != 0)
    print(f"Length: {len(naf)}")
    print(f"Non-zero digits: {non_zeros}")
    print(f"Zeros: {naf.count(0)}")
    print(f"Density (non-zeros/length): {non_zeros/len(naf):.2%}")

    return naf


def main():
    print("=" * 70)
    print("Non-Adjacent Form (NAF) Examples")
    print("=" * 70)

    print("\nWhat is NAF?")
    print("NAF is a signed binary representation where no two adjacent digits")
    print("are non-zero. This minimizes the number of non-zero digits, which")
    print("reduces the number of operations in cryptographic computations.")
    print("=" * 70)

    # Example 1: Small number
    print("\n1. Small Number Example:")
    print_naf_analysis(13)

    # Example 2: Power of 2
    print("\n2. Power of 2:")
    print_naf_analysis(16)

    # Example 3: Number with many 1s in binary
    print("\n3. Number with consecutive 1s in binary:")
    print_naf_analysis(31)  # 11111 in binary

    # Example 4: Larger number
    print("\n4. Larger Number:")
    print_naf_analysis(587257)

    # Example 5: Compare binary vs NAF efficiency
    print("\n5. Binary vs NAF Efficiency Comparison:")
    print("-" * 70)
    test_numbers = [15, 31, 63, 127, 255, 511, 1023]

    print(f"{'Number':<10} {'Binary 1s':<12} {'NAF Non-zeros':<15} {'Improvement':<12}")
    print("-" * 70)

    for n in test_numbers:
        binary_ones = bin(n).count('1')
        naf = bc.NAF(n)
        naf_nonzeros = sum(1 for x in naf if x != 0)
        improvement = (binary_ones - naf_nonzeros) / binary_ones * 100

        print(f"{n:<10} {binary_ones:<12} {naf_nonzeros:<15} {improvement:>5.1f}%")

    # Example 6: NAF Statistics
    print("\n6. NAF Statistics:")
    stats = bc.compute_naf_statistics(587257)
    print(f"Number: 587257")
    print(f"NAF representation: {stats['naf']}")
    print(f"Total length: {stats['length']}")
    print(f"Zeros: {stats['zeros']}")
    print(f"Probability of zero (p): {stats['p']:.3f}")
    print(f"Probability of non-zero (q_1): {stats['q_1']:.3f}")

    print("\n" + "=" * 70)
    print("\nKey Takeaways:")
    print("  - NAF reduces the number of non-zero digits")
    print("  - Fewer non-zero digits = fewer operations in exponentiation")
    print("  - Especially effective for numbers with consecutive 1s in binary")
    print("  - Critical optimization for elliptic curve cryptography")
    print("=" * 70)


if __name__ == "__main__":
    main()
