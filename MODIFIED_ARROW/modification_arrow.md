# Modified Arrow Source Code Explorations

This directory contains conceptual modifications to the Apache Arrow C++ core. These modifications were designed to test our hypotheses about Arrow's internal behavior and system limits. 

Due to the complex build process of the core C++ engine, these scripts act as our **System Modifications**, mapping directly to our experiments in Python and our Failure Analysis. 

## Included Modifications

### 1. `01_buffer_slice_logger.cc` (Execution Tracing)
- **Target File:** `cpp/src/arrow/buffer.cc`
- **Modification:** Added a `std::cout` logger natively inside the `Slice` function to trace whenever a zero-copy memory slice is initialized.
- **Relates to:** Experiment 2 (Buffer Memory Sharing). It proves at the lowest architecture level that Arrow is intercepting slice commands and just updating pointer offsets without moving data.

### 2. `02_memory_pool_cap.cc` (Failure Injection)
- **Target File:** `cpp/src/arrow/memory_pool.cc`
- **Modification:** Modified the `Allocate` function to manually throw an `OutOfMemory` exception when requested memory exceeds a hardcoded 50MB limit simulating a strict system constraint. 
- **Relates to:** Failure Analysis (Behavior under Data Size checks). 

### 3. `03_disable_zero_copy.cc` (System Isolation)
- **Target File:** `cpp/src/arrow/buffer.cc`
- **Modification:** We intentionally broke the `Slice` function to act as a deep copy (simulating a naive data system). Whenever a slice is called, we allocate new memory and use `std::memcpy()` to duplicate the data. 
- **Relates to:** Experiment 1 (Zero-Copy vs Copy). This conceptually turns Apache Arrow into a standard "copy-on-read" data system to evaluate the difference in O(n) scaling.
