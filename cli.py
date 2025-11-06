#!/usr/bin/env python3
"""
Command-line interface for addition-subtraction chains.

Provides easy access to chain generation from the command line.
"""

import argparse
import sys
import contfrac as cf
import gcf_chain as gcf
import bos_coster as bc


def generate_chain(args):
    """Generate an addition chain."""
    n = args.number

    if args.strategy:
        # Use strategy-based generation
        chain = gcf.minchain(n, args.strategy)
    elif args.parameter:
        # Use explicit parameter
        chain = cf.chain(n, args.parameter)
    else:
        # Use automatic optimal parameter
        k = cf.alpha(n)
        chain = cf.chain(n, k)

    # Display results
    print(f"Number: {n}")
    if not args.strategy and not args.parameter:
        print(f"Optimal parameter k: {cf.alpha(n)}")
    elif args.strategy:
        print(f"Strategy: {args.strategy}")

    print(f"\nChain: {chain}")
    print(f"Length: {len(chain)}")
    print(f"Bit length of n: {n.bit_length()}")
    print(f"Efficiency ratio: {len(chain) / n.bit_length():.2f}")


def compute_naf(args):
    """Compute NAF representation."""
    n = args.number
    naf = bc.NAF(n)

    print(f"Number: {n}")
    print(f"Binary: {bin(n)}")
    print(f"NAF: {naf}")
    print(f"\nLength: {len(naf)}")
    print(f"Non-zero digits: {sum(1 for x in naf if x != 0)}")
    print(f"Zeros: {naf.count(0)}")


def benchmark(args):
    """Benchmark chain generation."""
    import time

    n = args.number
    iterations = args.iterations

    print(f"Benchmarking chain generation for n={n}")
    print(f"Running {iterations} iterations...\n")

    start = time.time()
    for _ in range(iterations):
        k = cf.alpha(n)
        chain = cf.chain(n, k)
    elapsed = time.time() - start

    print(f"Total time: {elapsed:.6f} seconds")
    print(f"Average time per iteration: {elapsed/iterations:.6f} seconds")
    print(f"Operations per second: {iterations/elapsed:.2f}")
    print(f"\nFinal chain length: {len(chain)}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Addition-Subtraction Chains Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s chain 87                    # Generate chain for 87
  %(prog)s chain 1000 -s 1            # Use binary strategy
  %(prog)s chain 255 -k 15            # Use explicit parameter k=15
  %(prog)s naf 587257                 # Compute NAF representation
  %(prog)s benchmark 10000 -n 100     # Benchmark with 100 iterations

For more information, visit:
https://github.com/face-al/Addition-Subtraction-Chains
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # Chain generation command
    chain_parser = subparsers.add_parser('chain',
                                         help='Generate an addition chain')
    chain_parser.add_argument('number', type=int,
                             help='Target number (positive integer)')
    chain_parser.add_argument('-s', '--strategy', type=int,
                             choices=[1, 2],
                             help='Strategy: 1=Binary, 2=Square-root')
    chain_parser.add_argument('-k', '--parameter', type=int,
                             help='Explicit parameter k for chain generation')
    chain_parser.set_defaults(func=generate_chain)

    # NAF command
    naf_parser = subparsers.add_parser('naf',
                                       help='Compute Non-Adjacent Form')
    naf_parser.add_argument('number', type=int,
                           help='Number to convert to NAF')
    naf_parser.set_defaults(func=compute_naf)

    # Benchmark command
    bench_parser = subparsers.add_parser('benchmark',
                                         help='Benchmark chain generation')
    bench_parser.add_argument('number', type=int,
                             help='Target number for benchmark')
    bench_parser.add_argument('-n', '--iterations', type=int, default=1000,
                             help='Number of iterations (default: 1000)')
    bench_parser.set_defaults(func=benchmark)

    # Parse arguments
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        # Execute the command
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
