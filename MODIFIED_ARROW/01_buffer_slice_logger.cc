// TARGET FILE: cpp/src/arrow/buffer.cc
// PROJECT MODIFICATION: 01_buffer_slice_logger
// PURPOSE: Trace execution flow of zero-copy slice at the C++ level.

#include "arrow/buffer.h"
#include <iostream>  // [MODIFIED BY STUDENT] Added for tracing

namespace arrow {

// ... [existing arrow code boundaries] ...

Result<std::shared_ptr<Buffer>> SliceBuffer(const std::shared_ptr<Buffer>& buffer,
                                            int64_t offset, int64_t length) {
  if (offset < 0) {
    return Status::Invalid("Negative buffer slice offset");
  }
  if (length < 0) {
    return Status::Invalid("Negative buffer slice length");
  }
  
  // [MODIFIED BY STUDENT START]
  // Injecting an execution trace to log exactly when a zero-copy operation
  // occurs in the system, and calculating the raw memory offset being shifted.
  std::cout << "[SYSTEM TRACE] Zero-Copy Slice Initiated!" << std::endl;
  std::cout << " -> Original Buffer Address: " << (void*)buffer->data() << std::endl;
  std::cout << " -> Slice Offset Requested: " << offset << " bytes" << std::endl;
  // [MODIFIED BY STUDENT END]

  DCHECK_LE(offset, buffer->size());
  DCHECK_LE(offset + length, buffer->size());

  // Return a new buffer view pointing to the SAME physical memory block
  return std::make_shared<Buffer>(buffer, offset, length);
}

// ... [existing arrow code boundaries] ...

} // namespace arrow
