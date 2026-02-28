"""Command-line interface for computing concatenated binary value for a given n."""
import argparse
from .core import concatenated_binary


def main():
    parser = argparse.ArgumentParser(description="Compute concatenated binary from 1 to n.")
    parser.add_argument("n", type=int, help="Upper bound n (>=1)")
    args = parser.parse_args()
    print(concatenated_binary(args.n))


if __name__ == "__main__":
    main()
