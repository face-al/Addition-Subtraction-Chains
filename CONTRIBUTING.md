# Contributing to Addition-Subtraction Chains

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project follows a standard code of conduct:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive criticism
- Respect differing viewpoints and experiences

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a branch for your changes
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- git

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Addition-Subtraction-Chains.git
cd Addition-Subtraction-Chains

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Run tests to verify setup
python test.py
```

### Development Dependencies

For development, you may want additional tools:

```bash
pip install pytest pytest-cov  # For testing
pip install black              # For code formatting
pip install pylint             # For code linting
```

## How to Contribute

### Reporting Bugs

If you find a bug:

1. Check if the bug has already been reported in [Issues](https://github.com/face-al/Addition-Subtraction-Chains/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)
   - Code samples or test cases if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

1. Check existing issues/pull requests first
2. Create a new issue describing:
   - The enhancement and its benefits
   - Use cases
   - Potential implementation approach
   - Any drawbacks or concerns

### Contributing Code

Areas where contributions are especially welcome:

1. **New strategies**: Implement additional parameter selection strategies (Factor, Pi, Golden-ratio, etc.)
2. **Performance improvements**: Optimize existing algorithms
3. **Documentation**: Improve docstrings, examples, or README
4. **Tests**: Add more test cases for edge cases
5. **Bos-Coster algorithm**: Complete the partial implementation
6. **Bug fixes**: Fix reported issues

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use descriptive variable names
- Write docstrings for all public functions, classes, and modules
- Keep functions focused and reasonably sized

### Docstring Format

Use Google-style docstrings:

```python
def function_name(arg1, arg2):
    """
    Brief description of function.

    More detailed description if needed.

    Args:
        arg1 (type): Description of arg1
        arg2 (type): Description of arg2

    Returns:
        type: Description of return value

    Examples:
        >>> function_name(1, 2)
        3
    """
    pass
```

### Code Formatting

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black default)
- Use meaningful variable names
- Add comments for complex logic

### Example

```python
def compute_chain(n, k):
    """
    Generate addition chain for n using parameter k.

    Args:
        n (int): Target number
        k (int): Parameter for chain generation

    Returns:
        list: Addition chain from 1 to n
    """
    # Implementation here
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
python test.py

# Run with pytest (if installed)
pytest test.py -v

# Run with coverage
pytest test.py --cov=. --cov-report=html
```

### Writing Tests

- Add tests for all new functionality
- Test edge cases and error conditions
- Use descriptive test names
- Include docstrings explaining what is tested

Example test:

```python
def test_chain_for_power_of_2(self):
    """Test that powers of 2 generate optimal chains."""
    n = 16
    result = cf.minchain(n)
    expected = [1, 2, 4, 8, 16]
    self.assertEqual(result, expected)
```

## Pull Request Process

### Before Submitting

1. **Update your fork**:
   ```bash
   git remote add upstream https://github.com/face-al/Addition-Subtraction-Chains.git
   git fetch upstream
   git merge upstream/main
   ```

2. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
   - Write clear, focused commits
   - Follow coding standards
   - Add tests for new functionality
   - Update documentation as needed

4. **Test thoroughly**:
   ```bash
   python test.py
   ```

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

### Submitting Pull Request

1. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Go to GitHub and create a pull request

3. In the pull request description:
   - Describe what changes you made and why
   - Reference any related issues (e.g., "Fixes #123")
   - List any breaking changes
   - Describe how you tested the changes

### Pull Request Review

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

### After Merge

- Delete your feature branch
- Pull the latest changes from main
- Celebrate your contribution! 🎉

## Questions?

If you have questions:

1. Check the [README](README.md) and documentation
2. Search [existing issues](https://github.com/face-al/Addition-Subtraction-Chains/issues)
3. Create a new issue with your question

## Recognition

Contributors will be recognized in the project. Thank you for helping improve this library!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
