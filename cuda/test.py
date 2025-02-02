import numpy as np
from numba import cuda

# Define a CUDA kernel to add two arrays
@cuda.jit
def add_arrays_gpu(a, b, c):
    # Define the index in the array this thread will operate on
    idx = cuda.grid(1)
    if idx < a.size:  # Ensure the index is within bounds
        c[idx] = a[idx] + b[idx]

# Host code
n = 1024  # Array size
a = np.random.rand(n).astype(np.float32)  # Array A
b = np.random.rand(n).astype(np.float32)  # Array B
c = np.zeros_like(a)  # Output array C

# Allocate device memory and copy data to GPU
a_gpu = cuda.to_device(a)
b_gpu = cuda.to_device(b)
c_gpu = cuda.device_array_like(a)

# Configure the grid (number of threads and blocks)
threads_per_block = 256
blocks_per_grid = (a.size + threads_per_block - 1) // threads_per_block

# Launch the kernel
add_arrays_gpu[blocks_per_grid, threads_per_block](a_gpu, b_gpu, c_gpu)

# Copy the result back to host memory
c = c_gpu.copy_to_host()

# Verify the result
print("First 5 results (GPU):", c[:5])
print("First 5 results (CPU):", (a + b)[:5])
print("Results are the same:", np.allclose(c, a + b))
