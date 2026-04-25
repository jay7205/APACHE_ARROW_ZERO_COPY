import pyarrow as pa
import numpy as np
import time

# Bigger data
data = np.arange(50_000_000)

# Convert once
arr = pa.array(data)

# Zero-copy slice
start = time.time()
slice_arr = arr.slice(0, 25_000_000)
end = time.time()

print("Zero-copy slice time:", end - start)

# FORCE real copy using Python list (slow path)
start = time.time()
copy_arr = pa.array(list(data[:25_000_000]))
end = time.time()

print("Copy (forced) time:", end - start)