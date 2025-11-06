"""
Unit tests for addition-subtraction chains library.

Tests cover the core functionality of the contfrac module including
chain generation, GCF computation, and chain operations.
"""

import unittest
import contfrac as cf


class TestContinuedFraction(unittest.TestCase):
    """Test suite for continued fraction chain generation."""

    def test_chain_87(self):
        """
        Test chain generation for n=87.

        This is example 9.37 from Doche Chapter 9 p.162.
        The expected chain is the known optimal chain for 87.
        """
        n = 87
        k = cf.alpha(n)
        result = cf.chain(n, k)
        known = [1, 2, 3, 6, 7, 10, 20, 40, 80, 87]
        self.assertEqual(result, known,
                        f"Chain for {n} should match known optimal chain")

    def test_chain_29(self):
        """
        Test chain generation for n=29.

        Since addition chains are not unique, we only verify the length
        matches the known optimal chain length.
        """
        n = 29
        k = cf.alpha(n)
        result = cf.chain(n, k)
        known = [1, 2, 4, 8, 9, 17, 25, 29]

        # Verify the chain is valid (starts with 1, ends with n)
        self.assertEqual(result[0], 1, "Chain should start with 1")
        self.assertEqual(result[-1], n, f"Chain should end with {n}")

        # Verify chain length is optimal
        self.assertEqual(len(result), len(known),
                        f"Chain length for {n} should be {len(known)}")

    def test_minchain_power_of_2(self):
        """Test that powers of 2 generate optimal chains."""
        for power in [4, 5, 6, 7, 8]:
            n = 2 ** power
            result = cf.minchain(n)
            expected_length = power + 1
            self.assertEqual(len(result), expected_length,
                           f"Chain for 2^{power} should have length {expected_length}")
            self.assertEqual(result, [2**i for i in range(power + 1)],
                           f"Chain for 2^{power} should be [1,2,4,...,{n}]")

    def test_minchain_3(self):
        """Test special case for n=3."""
        result = cf.minchain(3)
        expected = [1, 2, 3]
        self.assertEqual(result, expected, "Chain for 3 should be [1,2,3]")

    def test_chain_validity(self):
        """
        Test that generated chains are valid.

        A valid chain must:
        1. Start with 1
        2. End with n
        3. Be sorted
        4. Have each element as sum/difference of previous elements
        """
        test_cases = [15, 31, 50, 100]

        for n in test_cases:
            k = cf.alpha(n)
            result = cf.chain(n, k)

            # Check starts with 1
            self.assertEqual(result[0], 1,
                           f"Chain for {n} should start with 1")

            # Check ends with n
            self.assertEqual(result[-1], n,
                           f"Chain for {n} should end with {n}")

            # Check sorted
            self.assertEqual(result, sorted(result),
                           f"Chain for {n} should be sorted")

            # Check all elements are positive
            self.assertTrue(all(x > 0 for x in result),
                          f"All elements in chain for {n} should be positive")

    def test_gcf(self):
        """Test generalized continued fraction computation."""
        # Test with coprime numbers
        result = cf.gcf(87, 10)
        self.assertEqual(len(result), 2, "GCF should return two coefficients")
        self.assertTrue(isinstance(result, list), "GCF should return a list")

    def test_product_operation(self):
        """Test chain product operation."""
        v = [1, 2, 4]
        w = [1, 2]
        result = cf.product(v.copy(), w.copy())

        # Should extend v with multiples of v[-1] * each element in w
        self.assertTrue(len(result) > len(v),
                       "Product should extend the chain")
        self.assertEqual(result[:3], [1, 2, 4],
                        "Product should preserve original chain elements")

    def test_addition_operation(self):
        """Test chain addition operation."""
        v = [1, 2, 3]
        j = 2
        result = cf.addition(v.copy(), j)

        expected_last = v[-1] + j
        self.assertEqual(result[-1], expected_last,
                        f"Last element should be {expected_last}")
        self.assertEqual(len(result), len(v) + 1,
                        "Addition should add one element")

    def test_subtraction_operation(self):
        """Test chain subtraction operation."""
        v = [1, 2, 3, 5]
        j = 2
        result = cf.subtraction(v.copy(), j)

        expected_last = v[-1] - j
        self.assertEqual(result[-1], expected_last,
                        f"Last element should be {expected_last}")
        self.assertEqual(len(result), len(v) + 1,
                        "Subtraction should add one element")

    def test_alpha(self):
        """Test alpha parameter computation."""
        test_cases = [29, 87, 256, 1000]

        for n in test_cases:
            result = cf.alpha(n)
            self.assertTrue(isinstance(result, int),
                          f"Alpha for {n} should return an integer")
            self.assertTrue(0 < result <= n,
                          f"Alpha for {n} should be in range (0, {n}]")

    def test_log_2(self):
        """Test log base 2 computation."""
        test_cases = {
            1: 0,
            2: 1,
            4: 2,
            8: 3,
            16: 4,
            255: 7,
            256: 8
        }

        for n, expected in test_cases.items():
            result = cf.log_2(n)
            self.assertEqual(result, expected,
                           f"log_2({n}) should be {expected}")


class TestGCFChain(unittest.TestCase):
    """Test suite for GCF chain with strategies."""

    def test_import(self):
        """Test that gcf_chain module can be imported."""
        try:
            import gcf_chain
            self.assertTrue(True)
        except ImportError:
            self.fail("Failed to import gcf_chain module")


class TestBOSCoster(unittest.TestCase):
    """Test suite for Bos-Coster NAF implementation."""

    def test_naf_zero(self):
        """Test NAF of zero."""
        import bos_coster as bc
        result = bc.NAF(0)
        self.assertEqual(result, [], "NAF of 0 should be empty list")

    def test_naf_small_numbers(self):
        """Test NAF for small numbers."""
        import bos_coster as bc

        # NAF of 1 should be [1]
        self.assertEqual(bc.NAF(1), [1])

        # NAF of 2 should be [1, 0] (least significant digit first)
        self.assertEqual(bc.NAF(2), [1, 0])

    def test_naf_properties(self):
        """Test that NAF satisfies its properties."""
        import bos_coster as bc

        test_numbers = [13, 31, 63, 127, 255]

        for n in test_numbers:
            naf = bc.NAF(n)

            # Check no adjacent non-zeros
            for i in range(len(naf) - 1):
                if naf[i] != 0:
                    self.assertEqual(naf[i + 1], 0,
                                   f"NAF of {n} should have no adjacent non-zeros")


def run_tests():
    """Run all tests with verbose output."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestContinuedFraction))
    suite.addTests(loader.loadTestsFromTestCase(TestGCFChain))
    suite.addTests(loader.loadTestsFromTestCase(TestBOSCoster))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
