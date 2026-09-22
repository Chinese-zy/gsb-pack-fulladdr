import unittest
from pack import pack
class T(unittest.TestCase):
    def test_same_prefix(self):
        boxes = pack([{"addr": "abc1", "name": "x"}, {"addr": "abc2", "name": "y"}])
        self.assertEqual(len(boxes), 1)
if __name__ == "__main__":
    unittest.main()
