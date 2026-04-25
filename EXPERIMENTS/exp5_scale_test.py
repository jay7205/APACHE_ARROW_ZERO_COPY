import pyarrow as pa
import numpy as np
import time

sizes = [1_000_000, 5_000_000, 10_000_000, 50_000_000]

for size in sizes:
    times = []

    for _ in range(3):  # repeat 3 times
        data = np.arange(size)

        start = time.time()
        arr = pa.array(data)
        end = time.time()

        times.append(end - start)

    avg_time = sum(times) / len(times)
    print(f"Size: {size}, Avg Time: {avg_time}")