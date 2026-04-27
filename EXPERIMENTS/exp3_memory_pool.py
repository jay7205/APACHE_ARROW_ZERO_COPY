import pyarrow as pa
import time

pool = pa.default_memory_pool()

print("Initial memory:", pool.bytes_allocated())

data = list(range(10_000_000))

arr1 = pa.array(data)
print("After arr1:", pool.bytes_allocated())

arr2 = pa.array(data)
print("After arr2:", pool.bytes_allocated())

del arr1
print("After deleting arr1:", pool.bytes_allocated())