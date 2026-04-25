# Apache Arrow — Zero-Copy System Analysis

## Overview

This project presents a system-level analysis of Apache Arrow, focusing on its zero-copy architecture. The goal is not to use the system as a tool, but to understand how it works internally by analyzing its codebase, tracing execution flow, and validating behavior through experiments.

The project follows a reverse-engineering approach, connecting code, system design, and real-world performance.

---

## Objective

This project aims to answer:

- What problem does Apache Arrow solve?
- How does zero-copy improve performance?
- What design decisions enable this behavior?
- What tradeoffs do these decisions introduce?
- How does the system behave under real-world conditions?

---

## Project Approach

The work was carried out in structured phases:

### Phase 1 — Execution Understanding
- Traced the execution path from Python API to memory
- Identified transition from Python layer to C++ layer
- Analyzed key components:
  - `array.pxi`
  - `ConvertPySequence`
  - `converter->Extend`
  - `ArrayData`
  - `Buffer`

---

### Phase 2 — Memory & Data Structures
- Studied how Arrow stores data in memory
- Key components:
  - Buffer → raw contiguous memory
  - ArrayData → metadata + buffers
- Identified how zero-copy is enabled through shared buffers

---

### Phase 3 — Design Decisions

Analyzed key architectural decisions:

1. Columnar memory layout  
2. Buffer abstraction  
3. Null bitmap handling  
4. Memory pool allocation  

Each decision was evaluated based on:
- Code location  
- Purpose  
- Tradeoffs  

---

### Phase 4 — Experiments

Conducted experiments to validate system behavior:

- Zero-copy vs copy performance  
- Buffer memory sharing  
- Memory pool behavior  
- Null bitmap impact  
- Large-scale behavior  
- Breaking zero-copy conditions  

---

### Phase 5 — Failure Analysis

Analyzed system limitations:

- Behavior under increasing data size  
- Conditions where zero-copy fails  
- Memory management tradeoffs  
- System assumptions  

---

## Key Findings

### Zero-Copy Behavior
- Zero-copy operations run in constant time (O(1))
- Copy operations scale linearly (O(n))
- Performance gain comes from avoiding memory duplication

---

### Memory Design
- Data stored in contiguous buffers
- Arrays act as views over memory
- Multiple arrays can share the same buffer

---

### System Boundaries
- Zero-copy works only within compatible memory formats
- Conversion to Python objects breaks zero-copy
- NumPy may preserve zero-copy depending on layout

---

### Memory Pool
- Memory is reused instead of freed immediately
- Improves performance but increases memory usage

---

### Real-World Behavior
- Performance influenced by:
  - CPU caching  
  - memory reuse  
  - runtime optimizations  
- Results are not always strictly linear  

---

## Experimental Results

### Zero-Copy vs Copy
- Zero-copy time remains constant  
- Copy time increases significantly with data size  

### Memory Pool
- Memory usage increases with allocation  
- Memory is reused after deletion  

### Breaking Zero-Copy
- Slice → zero-copy  
- Python list → copy  
- NumPy → conditional behavior  

### Scaling
- Performance trends exist but are influenced by system-level factors  

---

## System Diagrams

The following diagrams were generated programmatically:

- Execution Flow — API to memory pipeline  
- Memory Layout — ArrayData and buffers  
- Zero-Copy vs Copy — memory behavior  

Location:  
`DIAGRAMS/`

---

## Project Structure

```text
.
├── DESIGN_DECISION/
│   └── decision.md
│
├── DIAGRAMS/
│   ├── execution_flow.png
│   ├── generate diagrams.py
│   ├── memory_layout.png
│   └── zero_copy_vs_copy.png
│
├── EXPERIMENTS/
│   ├── exp1_zero_copy_vs_copy.py
│   ├── exp2_buffer_memory_check.py
│   ├── exp3_memory_pool.py
│   ├── exp4_null_bitmap.py
│   ├── exp5_scale_test.py
│   └── exp6_break_zero_copy.py
│
├── MODIFIED_ARROW/
│
├── PRESENTATION/
│
├── REPORT/
│   ├── concept_mapping.md
│   ├── execution_understanding.md
│   └── failure_analysis.md
│
├── RESULT/
│   ├── break_zero_copy_plot.png
│   ├── genarate_plot_experiments.py
│   ├── memory_pool_plot.png
│   ├── null_bitmap_plot.png
│   ├── observations.md
│   ├── scaling_plot.png
│   └── zero_copy_vs_copy_plot.png
│
└── README.md
```

## Technologies Used
Python (PyArrow, NumPy)
C++ (code analysis)
Matplotlib (visualization)
Apache Arrow source code
Key Insight

Apache Arrow achieves high performance not by faster computation, but by minimizing data movement in memory.

## Conclusion

This project demonstrates system-level understanding of Apache Arrow by:

tracing execution paths
analyzing internal data structures
validating behavior through experiments
identifying limitations and tradeoffs

The results highlight the importance of memory design in modern data systems.

## Author

Jay Patel — 202518025
Saachi Garg — 202518007

Student Project
M.Sc. Data Science — Big Data Analysis