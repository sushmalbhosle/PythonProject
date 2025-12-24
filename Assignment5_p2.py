

 
# 1. Create a list of numbers from 1 to 10
original_list = list(range(1, 11))

# 2. Extract the first five elements from the list
# Slicing the list from the beginning (index 0) up to, but not including, index 5
extracted_list = original_list[:5]

# 3. Reverses these extracted elements
# Using list slicing with a step of -1 to reverse the extracted list
reversed_list = extracted_list[::-1]

# 4. Prints both the extracted list and the reversed list
print("Extracted list:", extracted_list)
print("Reversed list:", reversed_list)