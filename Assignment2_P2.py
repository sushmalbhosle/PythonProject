# Initialize a variable to store the sum
total_sum = 0

# Loop through numbers from 1 to 50 (range function goes up to, but does not include, the end value)
for number in range(1, 51):
    total_sum += number  # Add the current number to the total_sum

# Print the final result
print(f"The sum of numbers from 1 to 50 is: {total_sum}")