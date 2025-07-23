import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertFalse(vitals_ok(99, 102, 70))
        


if __name__ == '__main__':
  unittest.main()
