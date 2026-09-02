"""Regression checks for the data-representation observations."""

from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest


DEMO_PATH = Path(__file__).with_name("demo.py")
SPEC = importlib.util.spec_from_file_location("data_representation_demo", DEMO_PATH)
assert SPEC and SPEC.loader
demo = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(demo)


class DataRepresentationTests(unittest.TestCase):
    def test_unsigned_eight_bit_values_wrap(self) -> None:
        self.assertEqual(demo.as_uint8(255), 255)
        self.assertEqual(demo.as_uint8(256), 0)
        self.assertEqual(demo.as_uint8(-1), 255)

    def test_observations_expose_representation_details(self) -> None:
        result = demo.observations()
        self.assertNotEqual(result["float_0_1_exact"], Fraction(1, 10))
        self.assertEqual(result["utf8_bytes"], [0xC3, 0x85])
        self.assertEqual(result["big_endian"], "1234")
        self.assertEqual(result["little_endian"], "3412")


if __name__ == "__main__":
    unittest.main()

