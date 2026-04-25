import pyarrow as pa
import numpy as np

print("=== Zero-Copy vs Break Zero-Copy ===")

# Create data
data = np.arange(10_000_000)
arr = pa.array(data)

# Case 1: Zero-copy slice
slice_arr = arr.slice(0, 5_000_000)

print("\n[CASE 1] Slice (Expected: ZERO-COPY)")
print("Original buffer:", arr.buffers()[1].address)
print("Slice buffer   :", slice_arr.buffers()[1].address)

if arr.buffers()[1].address == slice_arr.buffers()[1].address:
    print("Result: Zero-copy confirmed")
else:
    print("Result: Copy occurred")

# Case 2: Convert to Python list (FORCES COPY)
print("\n[CASE 2] Convert to Python list (Expected: COPY)")

py_list = arr.to_pylist()
new_arr = pa.array(py_list)

print("Original buffer:", arr.buffers()[1].address)
print("New array buffer:", new_arr.buffers()[1].address)

if arr.buffers()[1].address == new_arr.buffers()[1].address:
    print("Result: Zero-copy (unexpected)")
else:
    print("Result: Copy occurred (zero-copy broken)")

# Case 3: Convert to NumPy and back
print("\n[CASE 3] NumPy round-trip (Expected: COPY)")

np_array = arr.to_numpy()
arr_from_np = pa.array(np_array)

print("Original buffer:", arr.buffers()[1].address)
print("New array buffer:", arr_from_np.buffers()[1].address)

if arr.buffers()[1].address == arr_from_np.buffers()[1].address:
    print("Result: Zero-copy")
else:
    print("Result: Copy occurred")