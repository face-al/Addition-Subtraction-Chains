"""
Compare different strategies for chain generation.

This example demonstrates how different strategies affect chain generation
and allows comparison of their efficiency.
"""

import sys
sys.path.insert(0, '..')

import gcf_chain as gcf


def compare_strategies(n):
    """Compare different strategies for a given number."""
    print(f"\nGenerating chains for n = {n}")
    print("-" * 70)

    strategies = {
        1: "Binary Strategy (floor(n/2))",
        2: "Square-root Strategy (floor(sqrt(n)))"
    }

    results = {}

    for strategy_num, strategy_name in strategies.items():
        chain = gcf.minchain(n, strategy_num)
        results[strategy_num] = chain
        print(f"\n{strategy_name}:")
        print(f"  Chain: {chain}")
        print(f"  Length: {len(chain)}")

    return results


def main():
    print("=" * 70)
    print("Strategy Comparison for Addition Chain Generation")
    print("=" * 70)

    # Test with various numbers
    test_numbers = [63, 87, 100, 255, 500]

    for n in test_numbers:
        results = compare_strategies(n)

        # Find the best strategy
        best_strategy = min(results.keys(), key=lambda k: len(results[k]))
        print(f"\n  Best strategy for {n}: Strategy {best_strategy}")
        print(f"  Best chain length: {len(results[best_strategy])}")

    print("\n" + "=" * 70)
    print("\nStrategy Recommendations:")
    print("  - Binary Strategy: Good for general purpose, works well for most numbers")
    print("  - Square-root Strategy: Often produces shorter chains for larger numbers")
    print("=" * 70)


if __name__ == "__main__":
    main()
