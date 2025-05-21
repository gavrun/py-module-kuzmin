import argparse
import subprocess
import time
import statistics
import csv
import matplotlib.pyplot as plt
import os

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--dgemm", type=str, default="run_dgemm.py")
    parser.add_argument("--cycle", type=int, default=5)

    parser.add_argument("--in_a", type=str, required=True) # default="matrix_a.csv"
    parser.add_argument("--in_b", type=str, required=True) # default="matrix_b.csv"
    parser.add_argument("--in_c", type=str)                # default="matrix_c.csv" << rename "matrix_result.csv"
    parser.add_argument("--size", type=int, required=True)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--beta", type=float, default=0.0)
    parser.add_argument("--out_c", type=str, default="matrix_result.csv")
    
    parser.add_argument("--out_result", type=str, default="benchmark_results.csv")
    parser.add_argument("--out_plot", type=str, default="benchmark_plot.png")

    return parser.parse_args()

def run_benchmark(args):
    """Run DGEMM implementation and return execution time."""
    command = [
        "python", args.dgemm,
        "--in_a", args.in_a,
        "--in_b", args.in_b,
        "--size", str(args.size),
        "--alpha", str(args.alpha),
        "--beta", str(args.beta),
        "--out_c", args.out_c
    ]

    if args.in_c:
        command.extend(["--in_c", args.in_c])
    
    start = time.perf_counter()

    subprocess.run(command, check=True)

    end = time.perf_counter()

    return end - start

def save_csv(timing, filename):
    """Save execution timing results to a CSV file."""
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["run", "time_seconds"])
        for i, t in enumerate(timing, 1):
            writer.writerow([i, t])

def save_plot(timing, filename):
    """Create and save plot of execution results."""
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(timing)+1), timing, marker='o')
    plt.title("DGEMM Benchmark")
    plt.xlabel("Run")
    plt.ylabel("Time (seconds)")
    plt.grid(True)

    stats_text = (
        f"min={min(timing):.4f}s  "
        f"max={max(timing):.4f}s  "
        f"mean={statistics.mean(timing):.4f}s\n"
        f"median={statistics.median(timing):.4f}s  "
        f"stdev={statistics.stdev(timing) if len(timing) > 1 else 0:.4f}s"
    )

    plt.figtext(0.99, 0.01, stats_text, ha='right')
    plt.tight_layout()
    plt.savefig(filename)

def main():
    args = parse_args()

    timing = []

    for i in range(args.cycle):
        try:
            time_elapsed = run_benchmark(args)
            timing.append(time_elapsed)
        except subprocess.CalledProcessError:
            return

    save_csv(timing, args.out_result)

    save_plot(timing, args.out_plot)

#
if __name__ == "__main__":
    main()

# usage
# python launch_benchmark.py --in_a matrix_a.csv --in_b matrix_b.csv --size 10 
# python launch_benchmark.py --dgemm dgemm.py --cycle 10 --in_a matrix_a.csv --in_b matrix_b.csv --size 10 --alpha 0.5 --beta 1.0 --in_c matrix_c.csv
