# Addition-Subtraction Chains using Generalized Continued Fractions

A Python library for generating optimal addition-subtraction chains using Generalized Continued Fractions (GCF). This library is useful for optimizing exponentiation operations in cryptography, particularly in elliptic curve cryptography and modular exponentiation.

## What are Addition-Subtraction Chains?

An **addition-subtraction chain** for a positive integer `n` is a sequence of integers starting with 1 and ending with `n`, where each element is either the sum or difference of two previous elements in the sequence.

For example, an addition chain for 87 is: `[1, 2, 3, 6, 7, 10, 20, 40, 80, 87]`

These chains are essential for:
- **Fast exponentiation**: Computing x^n efficiently
- **Elliptic curve cryptography**: Scalar multiplication optimization
- **Modular arithmetic**: Reducing computational complexity

The goal is to find the **shortest possible chain** for any given number, which minimizes the number of operations needed.

## Features

- **Generalized Continued Fraction (GCF) Algorithm**: Core implementation based on academic research
- **Multiple Strategy Support**: Binary, square-root, factor, pi, golden-ratio strategies
- **NAF (Non-Adjacent Form)**: For signed binary representations
- **Bos-Coster Algorithm**: Partial implementation for alternative approach
- **Optimized Chain Generation**: Automatically selects optimal parameters

## Installation

### From Source

```bash
git clone https://github.com/face-al/Addition-Subtraction-Chains.git
cd Addition-Subtraction-Chains
pip install -r requirements.txt
pip install -e .
```

### Requirements

- Python 3.7+
- NumPy

## Quick Start

### Basic Usage

```python
import contfrac as cf

# Generate an optimal chain for n=87
n = 87
k = cf.alpha(n)  # Automatically determine optimal parameter
chain = cf.chain(n, k)
print(f"Chain for {n}: {chain}")
# Output: [1, 2, 3, 6, 7, 10, 20, 40, 80, 87]

# Generate a minimal chain
chain = cf.minchain(29)
print(f"Minimal chain for 29: {chain}")
# Output: [1, 2, 4, 8, 9, 17, 25, 29]
```

### Using Different Strategies

```python
import gcf_chain as gcf

# Strategy 1: Binary Strategy (floor(n/2))
chain1 = gcf.minchain(63, strategy_num=1)

# Strategy 2: Square-root Strategy (floor(sqrt(n)))
chain2 = gcf.minchain(63, strategy_num=2)

print(f"Binary Strategy: {chain1}")
print(f"Square-root Strategy: {chain2}")
```

### Working with NAF (Non-Adjacent Form)

```python
import bos_coster as bc

# Convert a number to NAF representation
n = 587257
naf = bc.NAF(n)
print(f"NAF of {n}: {naf}")
```

## API Reference

### `contfrac` Module

#### `chain(n, k)`
Generate an addition chain for integer `n` using parameter `k`.

- **Parameters:**
  - `n` (int): Target integer
  - `k` (int): Chain generation parameter
- **Returns:** List of integers forming the chain

#### `minchain(n)`
Generate a minimal or near-minimal addition chain for `n`.

- **Parameters:**
  - `n` (int): Target integer
- **Returns:** List of integers forming the chain

#### `alpha(n)`
Automatically determine the optimal parameter `k` for chain generation.

- **Parameters:**
  - `n` (int): Target integer
- **Returns:** Optimal parameter value

#### `gcf(n, k)`
Compute generalized continued fraction coefficients.

- **Parameters:**
  - `n` (int): First integer
  - `k` (int): Second integer
- **Returns:** List `[u1, u2]` of coefficients

#### `product(v, w)`
Combine two chains via multiplication operation.

- **Parameters:**
  - `v` (list): First chain
  - `w` (list): Second chain
- **Returns:** Combined chain

#### `addition(v, j)`
Extend chain by adding a value.

- **Parameters:**
  - `v` (list): Input chain
  - `j` (int): Value to add
- **Returns:** Extended chain

#### `subtraction(v, j)`
Extend chain by subtracting a value.

- **Parameters:**
  - `v` (list): Input chain
  - `j` (int): Value to subtract
- **Returns:** Extended chain

### `gcf_chain` Module

#### `minchain(n, strategy_num)`
Generate minimal chain using specified strategy.

- **Parameters:**
  - `n` (int): Target integer
  - `strategy_num` (int): Strategy selection (1=Binary, 2=Square-root)
- **Returns:** List of integers forming the chain

### `bos_coster` Module

#### `NAF(x)`
Convert integer to Non-Adjacent Form (NAF).

- **Parameters:**
  - `x` (int): Input integer
- **Returns:** List representing NAF with elements in {-1, 0, 1}

## Examples

See the `/examples` directory for more detailed usage examples:

- `basic_usage.py`: Simple chain generation
- `strategy_comparison.py`: Comparing different strategies
- `large_numbers.py`: Working with cryptographic-sized numbers

## Algorithm Details

This implementation is based on research by **Amadou Tall** on addition-subtraction chains using generalized continued fractions. The algorithm uses:

1. **Extended Euclidean Algorithm**: To compute GCD and Bézout coefficients
2. **Generalized Continued Fractions**: To decompose the problem recursively
3. **Dynamic Strategy Selection**: Multiple strategies for different number patterns

### Complexity

The chain length typically approaches `O(log n)`, making it efficient for large integers used in cryptographic operations.

## Testing

Run the test suite:

```bash
python -m pytest test.py
```

Or using unittest:

```bash
python test.py
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/face-al/Addition-Subtraction-Chains.git
cd Addition-Subtraction-Chains
pip install -r requirements.txt
python test.py
```

## References

- **Amadou Tall**: "Addition-Subtraction Chains using Generalized Continued Fractions"
- **Christophe Doche**: "Handbook of Elliptic and Hyperelliptic Curve Cryptography", Chapter 9

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

**Al Face** ([@face-al](https://github.com/face-al))

## Acknowledgments

This implementation is based on academic research by Amadou Tall with modifications and enhancements for practical use.

## Citation

If you use this library in your research, please cite:

```bibtex
@software{addition_subtraction_chains,
  author = {Face, Al},
  title = {Addition-Subtraction Chains using Generalized Continued Fractions},
  year = {2025},
  url = {https://github.com/face-al/Addition-Subtraction-Chains}
}
```
