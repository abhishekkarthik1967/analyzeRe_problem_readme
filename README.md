# Problem Statement
## Input

Input will consist of up to 100 lines of numbers - all decimal numbers
between 0.0 and 1,000,000,000.0 (inclusive).  The `compute` executable or
`compute.py` script must also accept two numerical arguments provided on
the command line.

The first argument will be referred as a `threshold` value. It will be a number
between 0.0 and 1,000,000,000.0 (inclusive).

The second argument will be referred to as the `limit` value. It will also be
between 0.0 and 1,000,000,000.0 (inclusive).

How to produce output from this input is described below.

## Output

The program __must only output numbers__.  Every line of output must contain
one (and only one) numerical value.  Do not output anything other than what
is required.  One number will be written for every number accepted via standard
input.  One extra number will be written at the very end, as explained below.

Since there are up to 100 lines of input (0 <= n <= 100), there will therefore
be n+1 lines of output expected from a valid solution.  The last line of output
(line n+1) will be a value that represents the cumulative sum of all the values
previously written.  The preceding output values will depend on the arguments,
which will be used to transform the input into the output.

### Example

Command line:

    # compute threshold limit
    compute 1000 20000000

Standard input:

    19.0
    0.0
    1000
    1001.5
    20000
    25000000.0

Standard output:

    0.0
    0.0
    0.0
    1.5
    19000.0
    19980998.5
    20000000.0

## Solution

## Steps to Run the Program in Different Environments

Create an `input.txt` file and copy the standard input format given in the problem statement. Then, execute the code using the following commands:

### Linux or MacOS
```sh
cat input.txt | python3 compute.py 1000 20000000.0 (linux or MacOS)
```

### Windows
```sh
type input.txt | python compute.py 1000 20000000.0 (Windows)
```

Make sure to replace `(linux or MacOS)` with the appropriate command for your operating system.

After executing the code, you will get the output as described in the problem statement.

Remember to save the `input.txt` file in the same directory as the `compute.py` script.

## Explanation of the Problem Statement

For each input value, compute the transformed value:

- Input: 19.0 → Output: `max(0.0, 19.0 - 1000) = 0.0`
- Input: 0.0 → Output: `max(0.0, 0.0 - 1000) = 0.0`
- Input: 1000 → Output: `max(0.0, 1000 - 1000) = 0.0`
- Input: 1001.5 → Output: `max(0.0, 1001.5 - 1000) = 1.5`
- Input: 20000 → Output: `max(0.0, 20000 - 1000) = 19000.0`
- Input: 25000000.0 → Output: `max(0.0, 25000000.0 - 1000) = 24999000.0`

But the cumulative sum constraint:
    Previous outputs sum: `0.0 + 0.0 + 0.0 + 1.5 + 19000.0 = 19001.5`
    Adding 24999000.0 exceeds the limit of 20000000.0.
    We can only add: `20000000.0 - 19001.5 = 19980998.5`.

So, the final output will be:
    Sum of all transformed values: `0.0 + 0.0 + 0.0 + 1.5 + 19000.0 + 19980998.5 = 20000000.0`

