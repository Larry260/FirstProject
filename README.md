# Number Analyzer

`analyzer.py` is a simple command-line script to analyze numeric lists.

## Features

- Prompts user for a comma-separated list of numbers.
- Prints original and sorted list (smallest to largest).
- Computes and prints:
  - Total
  - Count
  - Average
  - Minimum
  - Maximum
- Prints even numbers from the list (integer parity check).
- Graceful fallback to demo numbers when input is empty or invalid.

## Usage

```bash
python analyzer.py
```

Sample input:

```
Enter a list of numbers separated by commas (e.g. 3, 17, 5): 4, -1, 2.5, 8
```

## Behavior

- Numeric parsing via `float()`.
- Non-numeric input returns a validation message and uses demo list.
- Sorting uses Python built-in `sorted()`.

## Notes

- `even` check uses `num % 2 == 0`, which applies cleanly for integer values.
- `4.2` is not considered even by that definition (remainder 0.2).
