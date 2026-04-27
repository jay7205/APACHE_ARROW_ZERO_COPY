import pyarrow as pa
import numpy as np

data = np.arange(10_000_000)

arr = pa.array(data)

slice_arr = arr.slice(0, 5_000_000)

print("Original buffer address:", arr.buffers()[1].address)
print("Slice buffer address   :", slice_arr.buffers()[1].address)

if arr.buffers()[1].address == slice_arr.buffers()[1].address:
    print("Zero-copy confirmed: same memory buffer")
else:
    print("Different memory: copy occurred")