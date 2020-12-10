import unittest
from main import count_paths

class TestCountPaths(unittest.TestCase):
    def test_no_adapters(self):
        adapters = set()
        device = 3
        self.assertEqual(count_paths(0, device, adapters), 1)

    def test_one_adapter(self):
        adapters = {1}
        device = max(adapters) + 3
        self.assertEqual(count_paths(0, device, adapters), 1)

    def test_two_adapters_one_path(self):
        adapters = {2, 4}
        device = max(adapters) + 3
        self.assertEqual(count_paths(0, device, adapters), 1)

    def test_two_adapters_two_paths(self):
        adapters = {1, 2}
        device = max(adapters) + 3
        self.assertEqual(count_paths(0, device, adapters), 2)

    def test_example_data(self):
        adapters = set([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
        device = max(adapters) + 3
        self.assertEqual(count_paths(0, device, adapters), 8)

    def test_example_data_2(self):
        adapters = set([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23,
                        49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17,
                        7, 9, 4, 2, 34, 10, 3])
        device = max(adapters) + 3
        self.assertEqual(count_paths(0, device, adapters), 19208)


if __name__ == '__main__':
    unittest.main()
