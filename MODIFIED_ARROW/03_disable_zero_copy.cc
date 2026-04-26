// TARGET FILE: cpp/src/arrow/buffer.cc
// PROJECT MODIFICATION: 03_disable_zero_copy
// PURPOSE: Disable zero-copy and force a deep copy, directly changing the core algorithm.

#include "arrow/buffer.h"
#include <cstring>  // [MODIFIED BY STUDENT] Included for memcpy
#include <iostream>

namespace arrow {

// ... [existing arrow code boundaries] ...

Result<std::shared_ptr<Buffer>> SliceBuffer(const std::shared_ptr<Buffer>& buffer,
                                            int64_t offset, int64_t length) {
  if (offset < 0 || length < 0) {
    return Status::Invalid("Negative buffer slice offset or length");
  }

  DCHECK_LE(offset, buffer->size());
  DCHECK_LE(offset + length, buffer->size());

  // [MODIFIED BY STUDENT START]
  // Instead of passing the buffer pointer (zero-copy), we are explicitly 
  // allocating new memory and copying the data over (O(n) scaling)
  // to evaluate the baseline architectural advantage Arrow normally has.
  std::cout << "[ISOLATION TEST] Intentionally forcing a DEEP COPY during slice." << std::endl;

  uint8_t* new_data;
  ARROW_RETURN_NOT_OK(default_memory_pool()->Allocate(length, &new_data));
  std::memcpy(new_data, buffer->data() + offset, length);

  // We return a brand new buffer that owns its own data. This breaks zero copy!
  std::shared_ptr<Buffer> copied_buffer(new Buffer(new_data, length));
  return copied_buffer;
  // [MODIFIED BY STUDENT END]

  // (Original Arrow Code - Disabled)
  // return std::make_shared<Buffer>(buffer, offset, length);
}

// ... [existing arrow code boundaries] ...

} // namespace arrow
