import argparse
import random
import csv

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--type", choices=["float", "int"], default="float")
    parser.add_argument("--min", type=float, default=-10.0)
    parser.add_argument("--max", type=float, default=10.0)
    parser.add_argument("--out_a", type=str, default="matrix_a.csv")
    parser.add_argument("--out_b", type=str, default="matrix_b.csv")

    return parser.parse_args()

def generate_matrix(size, dtype, min_val, max_val):
    """Generate a square matrix of given size"""
    matrix = []
    for x in range(size):
        row = []
        for y in range(size):
            if dtype == "int": # not implemented
                value = random.uniform(min_val, max_val)
            else: # float
                value = random.uniform(min_val, max_val)
            row.append(value)
        matrix.append(row)
    
    return matrix

def save_csv(matrix, filename):
    """Save matrix to a CSV file"""
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

def main():
    args =  parse_args()

    matrix_a = generate_matrix(args.size, args.type, args.min, args.max)
    matrix_b = generate_matrix(args.size, args.type, args.min, args.max)

    save_csv(matrix_a, args.out_a)
    save_csv(matrix_b, args.out_b)

# main flow
if __name__ == "__main__":
    main()

# usage
# python generate_matrix.py --size 10
# python generate_matrix.py --size 10 --type float --min -100 --max 100 --out_a matrix_a.csv --out_b matrix_b.csv
