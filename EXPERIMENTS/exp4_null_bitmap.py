import pyarrow as pa
import time

data_no_null = list(range(10_000_000))
data_with_null = [i if i % 10 != 0 else None for i in data_no_null]

start = time.time()
arr1 = pa.array(data_no_null)
end = time.time()
print("No nulls time:", end - start)

start = time.time()
arr2 = pa.array(data_with_null)
end = time.time()
print("With nulls time:", end - start)