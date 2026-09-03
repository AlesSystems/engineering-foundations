# Contributing

This repository is a public learning notebook. Corrections, clearer explanations, stronger experiments, and primary sources are welcome.

## Content expectations

- Explain ideas in original language rather than reproducing source material.
- Distinguish facts, observations, interpretations, and opinions.
- Prefer reproducible experiments and primary sources.
- Give image, quotation, and adapted-diagram attribution.
- Never commit credentials, proprietary code, employer information, personal data, or copyrighted course solutions.
- Keep generated binaries small; prefer text-based diagram sources.

## File conventions

- Use lowercase kebab-case filenames. Conventional repository files such as `README.md`, `CONTRIBUTING.md`, `.gitignore`, GitHub templates, license files, and Python modules/tests that follow `snake_case` conventions are exceptions.
- Keep a diagram beside the note it explains when possible.
- Put standalone code experiments in `labs/<topic>/` with reproduction instructions.
- Use relative links for repository files and descriptive text for external links. Legal license text is exempt when it requires a canonical bare URL.

## Diagram workflow

- Invoke `$diagram-design` before creating or substantially revising a diagram.
- Choose the semantic pattern and visual type before drawing, and keep within that type's complexity budget.
- Store durable diagrams as self-contained HTML with inline SVG. Mermaid is appropriate only for temporary working sketches that will not remain as study evidence.
- Give every meaningful SVG a first-child `<title>`, a useful `<desc>`, and resolving `role="img"` and `aria-labelledby` attributes.
- Run `python3 ~/agent-library/skills/craft/diagram-design/scripts/self_check.py <diagram.html>` plus any type-specific verifier provided by the selected skill version, then inspect the result at desktop and narrow widths.
- Do not commit PNG or standalone SVG exports unless a named consumer needs them; HTML remains the source of truth.


## Commit style

Use small, coherent Conventional Commits, for example:

- `docs(memory): explain virtual address translation`
- `lab(networking): trace a TCP handshake`
- `fix(storage): correct write-ahead log ordering`
