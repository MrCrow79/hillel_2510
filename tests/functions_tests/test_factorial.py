# from lessons.lesson_08.exceptions_example import counter
import unittest
import sys
import pathlib


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))



from functions import factorial  # from шлях_до_файла_з_початку_проекта import фунція_з_файла


class FactorialTest(unittest.TestCase):

    def test_factorial_positive_simple(self):
        expected_result = 120
        actual_result = factorial(5)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
