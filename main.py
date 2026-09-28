# Define two sample sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Method 1: Using the symmetric_difference() method
result_method1 = set_a.symmetric_difference(set_b)

# Method 2: Using the ^ operator
result_method2 = set_a ^ set_b

# Display results
print("Set A:", set_a)
print("Set B:", set_b)
print("Symmetric Difference:", result_method1)
