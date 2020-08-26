# Coding Challenge Solution
Solution for Challenge 1 is in Q1.py and solution for Challenge 2 is in Q2.py.
Note that Q2 imports and reuses some functions from Q1.
Solution is tested using Python 3.8.5

# Running the code
```
python Q1.py tests/Q1/in_sample.csv output.csv
python Q2.py tests/Q2/in_sample.csv output.csv
```

**Note 1**: If your system defaults to python 2, you should replace `python` with `python3`.

**Note 2**: Relative paths are formatted for the Unix-based operating systems.
On Windows, you should probably use backslashes.

# Running the tests
```
python test.py
```
will run all the unit tests. Unit tests use the sample input and output files in the `tests` folder.

# Test Coverage
Install Python Coverage:
```
pip install coverage
```

Run:
```
coverage run -m unittest test.py
coverage report
coverage html
```

A pregenerated report is present at: `coverage_report/index.html`. Code coverage is 100%.

# Design
* Both solutions use binary search (`bisect` function in python) to find the insertion point of a number in a sorted array.
* Both solution have a time complexity of O(n * log(n)) (n being the total number of bonds)
* For interpolation, the slope of the line between the previous and the next point (in government bonds) is considered.

# Rooms for Imorovement (If I had more time)
* Write separate unit tests for CSV operations and data proccessing operations.
