import unittest


def square(n: int) -> int:
    return n * n


def cube(n: int) -> int:
    return n * n * n


def add(a: int, b: int) -> int:
    return a + b


class SquareTestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertNotEqual(square(4), 15)

    def test_cube(self):
        self.assertEqual(cube(4), 64)
        self.assertNotEqual(cube(4), 63)

    def test_add(self):
        self.assertEqual(add(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
