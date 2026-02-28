[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Concatenated Binary Numbers

Open source project for solving LeetCode problem "Concatenation of Consecutive Binary Numbers". This repository provides a clean, well-tested Python backend with a small API and a minimal frontend example. Contributions are welcome.

## Problem
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 1e9+7. See LeetCode problem: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

## Architecture
- core: concatenated_binary(n) exact algorithm using modular arithmetic
- api: FastAPI endpoint /calculate
- cli: simple command-line interface
- frontend: static HTML/JS that demonstrates API usage
- tests: pytest-based unit and API tests

## Setup
python -m venv venv
source venv/bin/activate  # on Unix
venv\\Scripts\\activate     # on Windows
pip install -r requirements.txt

## Running
# Run API
uvicorn concatenated_binary.api:app --reload --port 8000

# Run CLI
python -m concatenated_binary.cli 12

# Run tests
pytest

## Tests
The test suite covers basic correctness, edge cases, and API behavior.

## References
- LeetCode problem: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
