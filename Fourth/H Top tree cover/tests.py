import unittest
import psutil
import os
from time import perf_counter

from solution import solve
from cases import stress_case, cases


class TestSolution(unittest.TestCase):

    def test_solution(self):
        counter = 0
        for case, answer in cases:
            with self.subTest(f"Test case {counter}, case: {case}"):
                counter += 1
                result = solve(*case)
                self.assertEqual(answer, result)

    def test_performance(self):
        case, answer = stress_case
        time1 = perf_counter()
        result = solve(*case)
        time2 = perf_counter()
        print(f"Execution took {time2 - time1} sec")
        #self.assertEqual(answer, result)

    def test_memory(self):
        case, answer = stress_case
        result = solve(*case)
        process = psutil.Process(os.getpid())
        mem = process.memory_info()[0] / float(2 ** 20)
        print(f"Execution took {mem} MB")
        #self.assertEqual(answer, result)


if __name__ == "__main__":
    unittest.main()
