import pyarrow as pa
import numpy as np
import time

data = np.arange(50_000_000)

arr = pa.array(data)

start = time.time()
slice_arr = arr.slice(0, 25_000_000)
end = time.time()

print("Zero-copy slice time:", end - start)

start = time.time()
copy_arr = pa.array(list(data[:25_000_000]))
end = time.time()

print("Copy (forced) time:", end - start)