# Repository instructions

## Diagrams

- Invoke `$diagram-design` before creating or substantially revising a diagram.
- Use the canonical skill from `~/agent-library`; do not copy skill files into this repository.
- Keep standalone or editorial diagrams as self-contained HTML with inline SVG. Mermaid remains valid for simple, note-local diagrams that render clearly without manual layout.
- Follow the selected visual type's complexity budget and accessibility contract.
- Before committing an HTML/SVG diagram, run the skill's `scripts/self_check.py` and any type-specific verifier the selected skill version provides, then inspect the rendered result at desktop and narrow widths.
- Keep generated PNG or SVG exports out of the repository unless a consumer explicitly requires them; the HTML file remains the source of truth.
