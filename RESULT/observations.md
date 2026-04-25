# Experiment Results and Analysis

## Experiment 1: Zero-Copy vs Copy

### Observations

- Zero-copy slice time: ~0.000014 seconds  
- Copy (forced) time: ~11.56 seconds  

### Analysis

Zero-copy slicing is nearly instantaneous because it avoids duplicating data and only creates a new view over the same memory buffer.

In contrast, copying requires allocating new memory and duplicating all elements, resulting in significantly higher execution time.

### Key Insight

Zero-copy operations run in constant time O(1), while copy operations scale linearly O(n).

---

## Experiment 2: Buffer Memory Sharing

### Observations

- Original buffer address = Slice buffer address  
- Both arrays reference the same memory location  

### Analysis

The slice operation shares the same underlying buffer as the original array, confirming that no new memory is allocated.

### Key Insight

Arrow enables zero-copy by allowing multiple arrays to reference the same memory buffer.

---

## Experiment 3: Memory Pool Behavior

### Observations

- Initial memory: 0 bytes  
- After arr1: ~80 MB  
- After arr2: ~160 MB  
- After deleting arr1: ~80 MB  

### Analysis

Memory usage increases as arrays are created. After deleting one array, memory is not fully released.

This indicates that Arrow uses a memory pool which retains memory for reuse instead of returning it to the system immediately.

### Key Insight

Memory pooling improves performance by reducing allocation overhead, but can increase peak memory usage.

---

## Experiment 4: Null Bitmap Handling

### Observations

- No nulls time: ~1.02 seconds  
- With nulls time: ~0.48 seconds  

### Analysis

The result appears counterintuitive, as null handling is expected to introduce overhead. However:

- Arrow uses an efficient bitmap representation for null values  
- Memory layout differences may improve access patterns  
- Python-level overhead and data patterns influence timing results  

### Key Insight

System-level optimizations can lead to non-intuitive performance results, and high-level measurements may not always reflect expected theoretical behavior.

---

## Experiment 5: Large-Scale Behavior

### Observations

- 1M → ~0.089 sec  
- 5M → ~0.0011 sec  
- 10M → ~0.0023 sec  
- 50M → ~0.015 sec  

### Analysis

Execution time generally increases with data size, but not in a perfectly linear manner.

This is influenced by:
- CPU caching effects  
- memory reuse  
- runtime optimizations  
- measurement noise  

### Key Insight

Scalability trends exist, but simple timing experiments may not produce perfectly consistent results without controlled benchmarking.

---

## Experiment 6: Breaking Zero-Copy

### Observations

- Case 1 (Slice):
  - Same buffer address → zero-copy confirmed  

- Case 2 (Python list conversion):
  - Different buffer address → copy occurred  

- Case 3 (NumPy round-trip):
  - Same buffer address → zero-copy maintained  

---

### Analysis

- Slicing within Arrow preserves zero-copy by reusing the same buffer  
- Converting to a Python list breaks zero-copy because data is materialized into Python objects and then reconstructed  
- NumPy conversion does not always break zero-copy; when memory layout is compatible, Arrow can share memory with NumPy  

---

### Key Insight

Zero-copy is not universally guaranteed. It depends on whether operations remain within compatible memory representations.

---

## Final Conclusion

These experiments demonstrate that:

- Zero-copy significantly improves performance by eliminating data duplication  
- Arrow relies on shared memory buffers for efficient data access  
- Memory pools optimize allocation by reusing memory  
- System behavior can produce non-intuitive results due to optimizations  
- Zero-copy depends on maintaining compatibility across system boundaries  

Overall, Apache Arrow achieves high performance primarily through careful memory design and minimizing data movement.