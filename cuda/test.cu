#include <iostream>
__global__ void helloCUDA() {
    printf("Hello from CUDA Kernel!\n");
}
int main() {
    helloCUDA<<<1, 1>>>();
    cudaDeviceSynchronize();
    return 0;
}
