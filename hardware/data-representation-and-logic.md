# Data Representation and Digital Logic

**Status:** seed  
**Last reviewed:** 2026-09-02

## Questions

- How can the same bits represent a positive integer, a negative integer, text, or an instruction?
- Why do fixed-width integers wrap while many decimal fractions are only approximated in binary floating point?
- How do stateless logic gates become a computer that remembers?

## Current model

A bit has no intrinsic meaning beyond distinguishing two states. A representation supplies the agreement that gives a bit pattern meaning. The eight bits `11111111`, for example, can denote 255 as an unsigned integer, -1 in eight-bit two's complement, part of an instruction, or a component of some encoded value. The bits do not carry their type with them; hardware instructions and software context determine how to interpret them.

Fixed-width unsigned arithmetic works modulo \(2^n\). With eight bits, 255 plus 1 produces 0 because the ninth carry bit is outside the representation. Two's complement arranges signed values so the same binary addition circuit works for positive and negative integers, but the representable range remains finite.

Binary floating point stores a sign, significand, and exponent. Just as 1/3 repeats in base ten, 1/10 repeats in base two. A finite IEEE 754 value therefore approximates decimal `0.1`; arithmetic exposes the accumulated approximation. This is predictable representation behavior, not randomness.

Text encoding is another agreement. Unicode assigns code points to characters, while encodings such as UTF-8 map those code points to bytes. Character count, code-point count, and byte count can differ.

## Diagram

The [representation dependency map](data-representation-dependency-map.html) shows how physical state becomes bits and how representation rules give the same bit pattern different meanings.

Combinational gates calculate outputs from current inputs. Feedback and a clock allow state elements to retain a value, which turns logic into memory. Registers combine state elements; CPUs combine registers, arithmetic logic, control, and connections to memory.

## Experiment

Run the [data-representation lab](../labs/data-representation/README.md). It compares fixed-width wrapping, the exact stored value of a floating-point number, UTF-8 bytes, and byte order.

## Key trade-offs and failure modes

| Choice or condition | Benefit | Cost or risk |
| --- | --- | --- |
| Fixed width | Predictable storage and hardware operations | Finite range and wraparound/overflow |
| Binary floating point | Large dynamic range and efficient hardware arithmetic | Most decimal fractions are approximate |
| UTF-8 | ASCII-compatible, compact for common Latin text, universal repertoire | Variable-width characters complicate indexing and length |
| Native byte order | Efficient platform representation | Serialized data becomes platform-dependent unless order is specified |

## What I learned

- Meaning comes from a representation contract, not from the bits alone.
- Overflow, rounding, and encoding bugs often occur where two components assume different representation contracts.
- Digital logic connects directly to software behavior: arithmetic width, instruction interpretation, and memory layout remain visible at high levels.

## Open questions

- How does a CPU distinguish instructions from data in memory?
- Where do language runtimes detect overflow, and where do they permit wrapping?
- How are combinational propagation delay and clock frequency related?

## Sources

- Nisan and Schocken, [Nand2Tetris, Part I](https://www.nand2tetris.org/course), hardware chapters and projects, accessed 2026-09-02.
- IEEE, [IEEE 754-2019: Standard for Floating-Point Arithmetic](https://standards.ieee.org/ieee/754/6210/), overview, accessed 2026-09-02.
- Unicode Consortium, [Unicode Standard: Technical Introduction](https://www.unicode.org/standard/principles.html), accessed 2026-09-02.
