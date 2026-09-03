# Repository instructions

## Diagrams

- Invoke `$diagram-design` before creating or substantially revising a diagram.
- Use the canonical skill from `~/agent-library`; do not copy skill files into this repository.
- Keep durable diagrams as self-contained HTML with inline SVG. Use Mermaid only for temporary sketches where editorial layout adds no value.
- Follow the selected visual type's complexity budget and accessibility contract.
- Before committing a diagram, run the skill's `scripts/self_check.py` and any type-specific geometry verifier, then inspect the rendered result at desktop and narrow widths.
- Keep generated PNG or SVG exports out of the repository unless a consumer explicitly requires them; the HTML file remains the source of truth.
