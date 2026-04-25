import pyarrow as pa
import numpy as np

# Create data
data = np.arange(10_000_000)

# Convert to Arrow array
arr = pa.array(data)

# Slice (zero-copy)
slice_arr = arr.slice(0, 5_000_000)

# Print memory addresses
print("Original buffer address:", arr.buffers()[1].address)
print("Slice buffer address   :", slice_arr.buffers()[1].address)

# Check if same memory
if arr.buffers()[1].address == slice_arr.buffers()[1].address:
    print("Zero-copy confirmed: same memory buffer")
else:
    print("Different memory: copy occurred")