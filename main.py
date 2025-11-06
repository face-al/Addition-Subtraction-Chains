"""
Demonstration script for addition-subtraction chains library.

This script demonstrates various features of the library with examples.
For more detailed examples, see the examples/ directory.
"""

import contfrac as cf


def demo_basic_chains():
    """Demonstrate basic chain generation."""
    print("=" * 70)
    print("BASIC CHAIN GENERATION")
    print("=" * 70)

    # Example 1: Chain for 87 (from academic literature)
    print("\nExample 1: Chain for 87 (Doche Chapter 9, Example 9.37)")
    n = 87
    k = cf.alpha(n)
    chain = cf.chain(n, k)
    print(f"n = {n}, k = {k}")
    print(f"Chain: {chain}")
    print(f"Length: {len(chain)}")

    # Example 2: Using minchain
    print("\nExample 2: Using minchain for automatic optimization")
    n = 29
    chain = cf.minchain(n)
    print(f"n = {n}")
    print(f"Chain: {chain}")
    print(f"Length: {len(chain)}")


def demo_operations():
    """Demonstrate chain operations."""
    print("\n" + "=" * 70)
    print("CHAIN OPERATIONS")
    print("=" * 70)

    # Product operation
    print("\nProduct Operation:")
    v = [1, 2, 4]
    w = [1, 2]
    result = cf.product(v.copy(), w.copy())
    print(f"product({v}, {w}) = {result}")

    # Addition operation
    print("\nAddition Operation:")
    v = [1, 2, 3]
    j = 2
    result = cf.addition(v.copy(), j)
    print(f"addition({v}, {j}) = {result}")

    # Subtraction operation
    print("\nSubtraction Operation:")
    v = [1, 2, 3, 5]
    j = 2
    result = cf.subtraction(v.copy(), j)
    print(f"subtraction({v}, {j}) = {result}")


def demo_special_cases():
    """Demonstrate special cases."""
    print("\n" + "=" * 70)
    print("SPECIAL CASES")
    print("=" * 70)

    # Powers of 2
    print("\nPowers of 2 (optimal chains):")
    for power in [4, 5, 6, 7, 8]:
        n = 2 ** power
        chain = cf.minchain(n)
        print(f"2^{power} = {n:>4}: {chain}")

    # Small numbers
    print("\nSmall numbers:")
    for n in [3, 5, 7, 15]:
        k = cf.alpha(n)
        chain = cf.chain(n, k)
        print(f"n = {n:>2}: {chain}")


def demo_large_numbers():
    """Demonstrate with larger numbers."""
    print("\n" + "=" * 70)
    print("LARGE NUMBERS")
    print("=" * 70)

    test_cases = [
        (1000, "Thousand"),
        (10000, "Ten thousand"),
        (26235947428953663183191, "70-bit number")
    ]

    for n, description in test_cases:
        k = cf.alpha(n)
        chain = cf.chain(n, k)
        print(f"\n{description}: n = {n}")
        print(f"Bit length: {n.bit_length()}")
        print(f"Parameter k: {k}")
        print(f"Chain length: {len(chain)}")
        print(f"Efficiency ratio: {len(chain) / n.bit_length():.2f}")


def main():
    """Main demonstration function."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "ADDITION-SUBTRACTION CHAINS DEMONSTRATION" + " " * 16 + "║")
    print("╚" + "═" * 68 + "╝")

    demo_basic_chains()
    demo_operations()
    demo_special_cases()
    demo_large_numbers()

    print("\n" + "=" * 70)
    print("\nFor more examples, see:")
    print("  - examples/basic_usage.py")
    print("  - examples/strategy_comparison.py")
    print("  - examples/large_numbers.py")
    print("  - examples/naf_usage.py")
    print("\nTo use the CLI:")
    print("  python cli.py chain 87")
    print("  python cli.py naf 13")
    print("  python cli.py benchmark 1000")
    print("\nRun tests:")
    print("  python test.py")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
