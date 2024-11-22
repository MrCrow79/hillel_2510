# from lessons.lesson_08.exceptions_example import counter
import unittest
import sys
import pathlib
import logging


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))



from functions import factorial  # from шлях_до_файла_з_початку_проекта import фунція_з_файла


class FactorialNegativeTest(unittest.TestCase):
    logger = logging.getLogger(__name__)

    def test_factorial_negative(self):

        with self.assertRaises(TypeError):
            self.logger.warning('Trying call factorial function with str(5)')
            factorial('5')


if __name__ == '__main__':
    unittest.main()
