"""
My understanding from the problem statement is as below:
For each input value, compute the transformed value:
    Input: 19.0 → Output: max(0.0, 19.0 - 1000) = 0.0
    Input: 0.0 → Output: max(0.0, 0.0 - 1000) = 0.0
    Input: 1000 → Output: max(0.0, 1000 - 1000) = 0.0
    Input: 1001.5 → Output: max(0.0, 1001.5 - 1000) = 1.5
    Input: 20000 → Output: max(0.0, 20000 - 1000) = 19000.0
    Input: 25000000.0 → Output: max(0.0, 25000000.0 - 1000) = 24999000.0
    But the cumulative sum constraint:
        Previous outputs sum: 0.0 + 0.0 + 0.0 + 1.5 + 19000.0 = 19001.5
        Adding 24999000.0 exceeds the limit of 20000000.0.
        We can only add: 20000000.0 - 19001.5 = 19980998.5.
    So, the final output will be:
        Sum of all transformed values: 0.0 + 0.0 + 0.0 + 1.5 + 19000.0 + 19980998.5 = 20000000.0
"""


# Usage: cat input.txt | python3 compute.py 1000 20000000.0 (linux or MacOS)
# Usage: type input.txt | python compute.py 1000 20000000.0 (Windows)

import sys

def main():
    # Check if the correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: compute.py <threshold> <limit>")
        sys.exit(1)
    
    # Convert the command line arguments to float
    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])
    
    # Read numerical input values from standard input and convert them to a list of floats
    inputs = [float(line.strip()) for line in sys.stdin]

    # Initialize an empty list to store output values
    outputs = []

    cumulative_sum = 0.0
    
    for value in inputs:
        # Calculate the transformed value based on the threshold
        transformed_value = max(0.0, value - threshold)

        # Ensure the cumulative sum does not exceed the limit
        if cumulative_sum + transformed_value > limit:
            transformed_value = limit - cumulative_sum

        # Add the transformed value to the output list
        outputs.append(transformed_value)

        # Update the cumulative sum
        cumulative_sum += transformed_value

         # If the cumulative sum has reached the limit, stop processing further inputs
        if cumulative_sum >= limit:
            break
    
    for output in outputs:
        print(output)
    print(cumulative_sum)

if __name__ == "__main__":
    main()
