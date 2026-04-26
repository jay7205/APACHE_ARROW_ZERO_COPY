// TARGET FILE: cpp/src/arrow/memory_pool.cc
// PROJECT MODIFICATION: 02_memory_pool_cap
// PURPOSE: Inject a failure component to simulate tight memory constraints.

#include "arrow/memory_pool.h"
#include <iostream>

namespace arrow {

// ... [existing arrow code boundaries] ...

Status DefaultMemoryPool::Allocate(int64_t size, int64_t alignment, uint8_t** out) {
  if (size < 0) {
    return Status::Invalid("negative malloc size");
  }

  // [MODIFIED BY STUDENT START]
  // Injecting a system limit to simulate a crashed environment under heavy load.
  // We limit allocations to 50MB (50 * 1024 * 1024 bytes)
  const int64_t HARD_MEMORY_LIMIT = 52428800; // 50MB
  
  if (size > HARD_MEMORY_LIMIT) {
    std::cerr << "[FAILURE INJECTION] Attempted to allocate " << size 
              << " bytes, which exceeds the strict 50MB threshold." << std::endl;
    return Status::OutOfMemory("System threshold reached. Failing safely.");
  }
  // [MODIFIED BY STUDENT END]

  // Actual C++ malloc logic (simplified representation)
  *out = static_cast<uint8_t*>(std::malloc(size));
  if (*out == nullptr) {
    return Status::OutOfMemory("malloc of size ", size, " failed");
  }

  return Status::OK();
}

// ... [existing arrow code boundaries] ...

} // namespace arrow
