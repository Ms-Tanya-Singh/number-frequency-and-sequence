# number-frequency-and-sequence
Analyze a list of integers to find the most frequently occurring number and the longest consecutive repetition of the same number. Handles mixed input formats and common edge cases.

# Smallest Frequent Number and Longest Repetition Finder

This Python program performs two tasks on a list of integers:
1. Finds the most frequently occurring number. If there is a tie, the smallest number is returned.
2. Finds the longest consecutive repetition of the same number, and tells both the number and its repetition length.

## Features

- Accepts flexible input formats:
  - Space-separated integers: `5 2 2 3 3 3`
  - With brackets and commas: `[5, 2, 2, 3, 3, 3]`
  - Mixed formatting: `5, 2 2,3`
- Graceful handling of edge cases:
  - Empty input: program exits with a message
  - Non-integer entries: program exits with a message
  - Single number input: both functions still return valid output

## Example Input and Output

### Input:
```
[3, 2, 2, 4, 3, 2, 2, 2]
```

### Output:
```
The smallest frequently occurring number is 2 and its frequency is 5
The longest same-number sequence is of number 2 and its length is 4
```

### Input:
```
5 a 2
```

### Output:
```
Please enter only integers.
```

### Input:
```
[ ]
```

### Output:
```
The list is empty.
```

## How to Run

1. Save the code to a file named `main.py`
2. Run in terminal or IDE using Python 3:
```
python main.py
```

## Python Version

This program is written in Python 3 and tested with Python 3.8+

