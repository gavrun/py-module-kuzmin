# Benchmark

Basic Python implementation of GEMM benchmark using pure nested loops for operations in double precision (64-bit floating point).

## refs

Matrix multiplication https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm

GEMM (General Matrix Multiplication) optimized

DGEMM (Double Precision General Matrix Multiplication) https://iq.opengenus.org/dgemm/

Formula:

```
C = α·A·B + β·C
```
where:

- A, B, and C - square matrices of size N x N

- alpha, beta - scalar values (alpha = 1.0 and beta = 0.0 used for benchmarking)


## DGEMM algorithm 

```
Function DGEMM(A[N][N], B[N][N], C[N][N], alpha, beta):
    for i from 0 to N-1:
        for j from 0 to N-1:
            sum = 0.0
            for k from 0 to N-1:
                sum = sum + A[i][k] * B[k][j]
            C[i][j] = alpha * sum + beta * C[i][j]

```

## generator

Generates two matrices A and B of given size and outputs them to separate .csv files. C matrix is optional.

Using [argparse] and [random] and [csv]

## single-threaded implementation

Manual matrix multiplication using the DGEMM reference algorithm after loading matrices from .csv files and checking their sizes.

## launcher and analyzer

Repeated execution of DGEMM implementation and measuring basic statistics outputting to .csv file

