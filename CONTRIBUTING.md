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

- Use lowercase kebab-case filenames. Conventional repository files such as `README.md`, `CONTRIBUTING.md`, `.gitignore`, GitHub templates, and license files are exceptions.
- Keep a diagram beside the note it explains when possible.
- Put standalone code experiments in `labs/<topic>/` with reproduction instructions.
- Use relative links for repository files and descriptive text for external links. Legal license text is exempt when it requires a canonical bare URL.


## Commit style

Use small, coherent Conventional Commits, for example:

- `docs(memory): explain virtual address translation`
- `lab(networking): trace a TCP handshake`
- `fix(storage): correct write-ahead log ordering`
