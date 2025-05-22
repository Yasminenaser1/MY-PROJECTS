# Part 1: Calculating Error

# 1. Define get_y()
def get_y(m, b, x):
    return m * x + b

# Test get_y()
print(get_y(1, 0, 7))   # should be 7
print(get_y(5, 10, 3))  # should be 25

# 2. Define calculate_error()
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y_line = get_y(m, b, x_point)
    return abs(y_line - y_point)

# 4. Test calculate_error()
print(calculate_error(1, 0, (3, 3)))    # should be 0
print(calculate_error(1, 0, (3, 4)))    # should be 1
print(calculate_error(1, -1, (3, 3)))   # should be 1

# 5. Define calculate_all_error()
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error

# 6. Test calculate_all_error()
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print(calculate_all_error(1, 0, datapoints))  # expected output may vary
print(calculate_all_error(0.4, 1.6, datapoints))  # should be 5.0

# Part 2: Try a bunch of slopes and intercepts!

# 8. List of possible ms
possible_ms = [m * 0.1 for m in range(-100, 101)]

# 9. List of possible bs
possible_bs = [b * 0.1 for b in range(-200, 201)]

# 10. Initialize variables to track best line
smallest_error = float("inf")
best_m = 0
best_b = 0

# 11. Find best m and b through brute-force search
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

# 12. Print best m, b, and error
print("Best m:", best_m)
print("Best b:", best_b)
print("Smallest error:", smallest_error)

# Part 3: What does our model predict?

# 13. Predict bounce height of a 6cm ball
x = 6
predicted_y = get_y(best_m, best_b, x)
print("Predicted bounce height for 6cm ball:", predicted_y)
