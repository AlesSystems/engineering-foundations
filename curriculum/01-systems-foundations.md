# Cycle 1: Systems Foundations

## Intent

Build a connected mental model of what happens between source code and a reliable networked service. The cycle is designed for an experienced software engineer and assumes approximately five flexible hours per week.

There are no overdue weeks. If life interrupts the cycle, resume the next unfinished session.

## Weekly rhythm

- **Understand — 90 minutes:** read or watch selectively; capture questions, not transcripts.
- **Investigate — 90 minutes:** inspect a running system or build a small experiment.
- **Explain — 60 minutes:** write the topic in your own words and draw its model.
- **Review — up to 60 minutes:** retrieve from memory, refine, or leave explicit questions.

## Schedule

Unless a week explicitly says otherwise, its artifact follows the [topic note template](../templates/topic-note.md) and includes all four forms of evidence: an own-words explanation, a diagram, a practical experiment, and sourced conclusions with open questions.

### Week 1 — Bits, data representation, and digital logic

**Questions:** How does physical state represent information? Why do integer overflow, floating-point error, endianness, and text encoding surprise programs?

**Core topics:** binary and hexadecimal; two's complement; IEEE 754 intuition; character encoding; Boolean algebra; gates, adders, registers, and clocks.

**Lab:** encode and decode values by hand, observe overflow and floating-point behavior in a familiar language, then build or simulate a half-adder.

**Artifact:** begin with the seeded [data representation and logic note](../hardware/data-representation-and-logic.md) and extend its gate-to-register diagram and [companion lab](../labs/data-representation/README.md).

### Week 2 — CPU, instruction sets, and the life of a program

**Questions:** What does a CPU actually execute? How do compiler, assembler, linker, loader, and runtime divide responsibility?

**Core topics:** fetch-decode-execute; registers; instructions; stack and calling conventions; machine code; compilation pipeline; interrupts.

**Lab:** compile a tiny program, inspect assembly and symbols, and trace one function call.

**Artifact:** `hardware/program-to-instruction.md` with a source-to-process pipeline.

### Week 3 — Memory hierarchy and virtual memory

**Questions:** Why is memory access not uniform? How can every process appear to own a large contiguous address space?

**Core topics:** registers, caches, RAM, and storage; locality; cache lines; pages; address translation; TLB; allocation; stack versus heap.

**Lab:** benchmark sequential versus random access and inspect a process's memory map.

**Artifact:** `hardware/memory-hierarchy.md` with latency and address-translation models.

### Week 4 — Processes, kernels, and system calls

**Questions:** What protection boundary does the OS provide? What happens when code opens a file or starts another process?

**Core topics:** kernel and user mode; processes and threads; system calls; context switches; signals; permissions; process lifecycle.

**Lab:** trace a small command's system calls and inspect its process tree, descriptors, and exit status.

**Artifact:** `systems/processes-and-system-calls.md` with a user/kernel sequence diagram.

### Week 5 — Concurrency and scheduling

**Questions:** Which interleavings are possible? What makes shared state safe—or impossible to reason about?

**Core topics:** concurrency versus parallelism; scheduler; race conditions; atomicity; locks; condition variables; deadlock; message passing; structured concurrency.

**Lab:** reproduce a race, repair it, and document the invariant that the repair protects.

**Artifact:** `systems/concurrency.md` with a happens-before diagram.

### Week 6 — Storage and file systems

**Questions:** What does “written” mean? How do systems survive interruption between multiple writes?

**Core topics:** blocks; files and directories; inodes or equivalent metadata; buffering; durability; journaling; copy-on-write; checksums; RAID and backups.

**Lab:** inspect file metadata and descriptors, compare buffered and synced writes, and diagram a crash-consistency failure.

**Artifact:** `systems/storage-and-filesystems.md`.

### Week 7 — Networking from frames to transport

**Questions:** How does a byte travel to another machine? Where can it be delayed, duplicated, reordered, or lost?

**Core topics:** layering; Ethernet/Wi-Fi intuition; MAC and ARP/NDP; IP; routing; ports; UDP; TCP handshake, reliability, flow control, and congestion control.

**Lab:** capture DNS and TCP traffic, identify each layer, then build a tiny TCP client or server.

**Artifact:** `systems/networking-fundamentals.md` with a packet-encapsulation diagram.

### Week 8 — DNS, HTTP, TLS, and the web request

**Questions:** What happens after entering a URL? Which guarantees come from DNS, HTTP, and TLS—and which do not?

**Core topics:** recursive name resolution and caching; HTTP semantics; connection reuse; certificates; TLS handshake; proxies; load balancers; CDNs.

**Lab:** use command-line tools to trace DNS, certificate, request, redirect, and timing behavior for one site.

**Artifact:** `systems/web-request-lifecycle.md` with an end-to-end sequence diagram.

### Week 9 — Database internals and transactions

**Questions:** How do indexes trade writes and space for reads? What does a transaction promise under concurrency and failure?

**Core topics:** pages; B-trees and LSM trees; query plans; write-ahead logging; ACID; isolation anomalies; MVCC; normalization.

**Lab:** create a small relational dataset, compare query plans before and after an index, and demonstrate one isolation anomaly if practical.

**Artifact:** `systems/database-internals.md`.

### Week 10 — Distributed systems fundamentals

**Questions:** What changes when delay is unbounded and partial failure is normal? Which consistency guarantee does an application truly need?

**Core topics:** failure models; time and ordering; idempotency; retries; replication; partitions; consistency models; consensus intuition; queues and backpressure.

**Lab:** build a small unreliable client/server simulation with timeouts, duplicate delivery, retries, and idempotency keys.

**Artifact:** `systems/distributed-systems.md` with failure and retry timelines.

### Week 11 — Security, observability, and operations

**Questions:** How do we know a system is healthy? How do identity, least privilege, and layered defenses constrain failure?

**Core topics:** threat modeling; authentication versus authorization; secrets; input trust boundaries; logs, metrics, and traces; SLI/SLO intuition; deployment, rollback, backup, and recovery.

**Lab:** threat-model a small service, add structured logs and one metric, then write a failure-and-recovery drill.

**Artifact:** `systems/security-reliability-and-operations.md`.

### Week 12 — Synthesis: explain one request end to end

**Challenge:** choose a real service you know. Trace one user action from input through application code, runtime, system calls, CPU and memory, network, database, observability, and response. Include at least three failure paths and their recovery behavior.

**Agentic extension:** ask an AI agent to critique the explanation. Treat every claim as untrusted until verified against a primary source or experiment. Record where the agent helped, hallucinated, or needed better context.

**Artifacts:** `notes/end-to-end-request.md`, a complete architecture/sequence diagram, and a [cycle review](../templates/cycle-review.md).

## Completion signal

The cycle is complete when you can explain the end-to-end request without relying on vocabulary you cannot define. Unfinished subtopics move into the roadmap; they do not block completion.
