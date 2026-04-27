# Execution Understanding

## Overview

This section traces a complete execution path in Apache Arrow, from a user-level API call to the final in-memory representation of data. The goal is to understand how data flows through the system and how it is stored in memory.

---

## Execution Path: Python Input to Memory Storage

![Execution Flow](../DIAGRAMS/execution_flow.png)

This architectural diagram traces the entry point from the high-level Python `pa.array` call downwards, skipping intermediate abstractions directly into the C++ `Buffer` memory struct.

We trace the execution of the following input:

```python
pa.array([1, 2, 3])


Step 1: Python API Entry Point
Function: pa.array()
File: python/pyarrow/array.pxi

This is the user-facing entry point. It accepts input data and determines how it should be processed.


Step 2: Python Layer Processing
array() → _sequence_to_array()
File: python/pyarrow/array.pxi

The system identifies that the input is a Python sequence and prepares it for conversion. At this stage, no heavy computation is performed.


Step 3: Transition to C++ Layer
ConvertPySequence()
File: cpp/src/arrow/python/python_to_arrow.cc

This function marks the transition from Python to C++. It converts Python objects into Arrow-compatible structures and initiates core processing.


Step 4: Converter Creation
MakeConverter()
File: cpp/src/arrow/python/python_to_arrow.cc

A type-specific converter is created based on inferred data type. This converter defines how input values will be processed.


Step 5: Data Processing
converter->Extend()
File: cpp/src/arrow/python/python_to_arrow.cc

This is the core computation step. The converter iterates through the input sequence and appends values into Arrow’s internal structures.



Step 6: Array Construction
converter->ToChunkedArray()
File: cpp/src/arrow/python/python_to_arrow.cc

The processed data is assembled into an Arrow array object.



Step 7: Structured Representation
ArrayData
File: cpp/src/arrow/array/data.h

The array is represented using the ArrayData structure, which organizes metadata and buffers.



Key components:

buffers[0] → null bitmap
buffers[1] → actual values
Step 8: Memory Storage
Buffer
Files:
cpp/src/arrow/buffer.h
cpp/src/arrow/buffer.cc

Data is stored in contiguous memory buffers. These buffers hold raw bytes and enable efficient access and sharing of memory.

Final Execution Flow
pa.array()
→ array.pxi
→ _sequence_to_array
→ ConvertPySequence
→ MakeConverter
→ converter->Extend
→ ToChunkedArray
→ ArrayData
→ Buffer (memory)

---

## Execution Path: Memory Read to Python Output

Just as data is ingested into memory, it must be read back out. Here is the query trace of retrieving an element (`val = arr[0]`):

1. **Python Access:** `array.pxi` -> `__getitem__` is triggered natively.
2. **C++ Query:** Arrow fires `GetScalar`, which bypasses arrays checking length bounds and fetches the target `ArrayData` struct.
3. **Memory Access:** Dereferences the low-level `Buffer[1]` pointer to return the raw byte directly back into Python context.