# Long-term Roadmap

The roadmap is a direction, not a backlog. Plan one cycle at a time and revise the next cycle using evidence from the previous review.

## Cycle 1 — Systems foundations

Follow [the first 12-week cycle](01-systems-foundations.md): hardware to operating systems, networks, storage, databases, distributed systems, security, and operations.

## Cycle 2 — Software and computer-science foundations

- Data structures, complexity, and algorithmic trade-offs
- Programming-language semantics, types, interpreters, and compilers
- Functional, object-oriented, data-oriented, and concurrent models
- API and module design, coupling, cohesion, invariants, and testing
- Software architecture, evolution, refactoring, and technical debt
- Formal reasoning basics: logic, state machines, specifications, and property-based testing

**Suggested synthesis:** implement and explain a small interpreter or storage engine, including tests and performance trade-offs.

## Cycle 3 — Production engineering

- Linux administration and troubleshooting
- Containers, namespaces, cgroups, and orchestration
- Infrastructure as code and delivery pipelines
- Identity, access control, cryptography, and application security
- Observability, capacity, performance, SLOs, and incident response
- Cloud architecture, cost, resilience, backup, and disaster recovery

**Suggested synthesis:** deploy, observe, secure, load-test, break, and recover a small service.

## Cycle 4 — Agentic engineering

- Transformer and language-model intuition
- Tokens, context, sampling, embeddings, and retrieval
- Tool use, structured outputs, state, memory, and orchestration
- Task decomposition, context engineering, and human approval boundaries
- Evaluation design, graders, regression suites, and observability
- Prompt injection, data leakage, permissions, sandboxing, and supply-chain risk
- Cost, latency, reliability, fallback, and model selection
- Product patterns for human-agent collaboration

**Suggested synthesis:** build a narrow coding agent with tools, permissions, an evaluation set, traces, and a written threat model.

## Later depth tracks

- Computer architecture: pipelining, branch prediction, coherence, SIMD/GPU, and accelerators
- Networking: routing protocols, QUIC, software-defined networking, and network security
- Data systems: execution engines, replication, streaming, warehousing, and data governance
- Theory: discrete math, automata, computability, complexity, information, and probability
- Hardware and IT: electronics, buses, peripherals, firmware, virtualization, storage arrays, and datacenters

