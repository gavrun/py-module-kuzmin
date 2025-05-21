import argparse
import csv

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--in_a", type=str, required=True) # default="matrix_a.csv"
    parser.add_argument("--in_b", type=str, required=True) # default="matrix_b.csv"
    parser.add_argument("--in_c", type=str)                # default="matrix_c.csv" << rename "matrix_result.csv"
    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--beta", type=float, default=0.0)
    parser.add_argument("--out_c", type=str, default="matrix_result.csv")
    #parser.add_argument("--out_b", type=str, default="matrix_b.csv")

    return parser.parse_args()

def load_csv(path):
    """Load matrix from a CSV file."""
    matrix = []
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            matrix.append([float(value) for value in row])
    return matrix

def check_matrix(matrix, size):
    """Ensure matrix is of N x N format."""
    # valid_size = False
    if len(matrix) != size:
        raise ValueError
    for row in matrix:
        if len(row) != size:
            raise ValueError
    # valid_size = True
    # return valid_size   

def save_csv(matrix, path):
    """Save matrix to a CSV file."""
    with open(path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

def dgemm(in_a, in_b, size, alpha, beta, in_c=None):
    """Create matrix C (empty or copy from 'in_c' matrix) and run DGEMM algorithm"""
    c_result = [[0.0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            sum_product = 0.0
            for k in range(size):
                sum_product += in_a[i][k] * in_b[k][j]
            if in_c:
                c_result[i][j] = alpha * sum_product + beta * in_c[i][j]
            else:
                c_result[i][j] = alpha * sum_product 
    return c_result

def main():
    args = parse_args()

    a_init = load_csv(args.in_a)
    b_init = load_csv(args.in_b)

    check_matrix(a_init, args.size)
    check_matrix(b_init, args.size)

    if args.in_c:
        c_init = load_csv(args.in_c)
        check_matrix(c_init, args.size)
    else:
        c_init = None

    c_prod = dgemm(a_init, b_init, args.size, args.alpha, args.beta, c_init)
    
    save_csv(c_prod, args.out_c)

#
if __name__ == "__main__":
    main()

# usage
# python dgemm.py --in_a matrix_a.csv --in_b matrix_b.csv --size 10
# python dgemm.py --in_a matrix_a.csv --in_b matrix_b.csv --size 10 --alpha 0.5 --beta 1.0 --in_c matrix_c.csv --out_c matrix_c.csv 
