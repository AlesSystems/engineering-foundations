# Data Representation Lab

This small Python lab makes four representation details observable without third-party dependencies.

## Question

How do fixed-width integers, binary floating point, UTF-8, and byte order affect the values a program observes?

## Prediction

- Eight-bit unsigned arithmetic wraps after 255.
- The stored binary value for `0.1` is not exactly the rational number 1/10.
- `Å` occupies more than one UTF-8 byte.
- The same integer has different byte sequences in big- and little-endian order.

## Reproduction

From the repository root:

```sh
python3 labs/data-representation/demo.py
python3 -m unittest labs/data-representation/test_demo.py
```

## Observations to capture

- Which output differs from the value's familiar decimal presentation?
- Which results are language behavior, and which model fixed-width machine behavior explicitly?
- Does `sys.byteorder` match either explicit serialization order?

## Limitations

Python integers have arbitrary precision, so `as_uint8` explicitly models an eight-bit unsigned machine value. This lab does not demonstrate language-level integer overflow in C, Rust, Java, or another fixed-width runtime.

