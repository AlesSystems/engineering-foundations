"""Observable examples for Week 1: data representation."""

from fractions import Fraction
import sys


def as_uint8(value: int) -> int:
    """Return the value represented modulo 2**8."""
    return value & 0xFF


def observations() -> dict[str, object]:
    value = 0x1234
    character = "Å"
    return {
        "uint8_255_plus_1": as_uint8(255 + 1),
        "float_sum": 0.1 + 0.2,
        "float_0_1_exact": Fraction.from_float(0.1),
        "utf8_bytes": list(character.encode("utf-8")),
        "utf8_length": len(character.encode("utf-8")),
        "big_endian": value.to_bytes(2, byteorder="big").hex(),
        "little_endian": value.to_bytes(2, byteorder="little").hex(),
        "native_byteorder": sys.byteorder,
    }


if __name__ == "__main__":
    for name, value in observations().items():
        print(f"{name}: {value}")

