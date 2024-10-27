def calculate_time_complexity(arr):
    n = len(arr)
    
    # Outer loop runs 'n' times
    for i in range(n):
        # Inner loop runs 'n' times for each iteration of the outer loop
        for j in range(n):
            print("Processing element:", arr[i] * arr[j])  # Example operation
    
    print("Time complexity of the code snippet: O(n^2)")

# Example usage
array = [1, 2, 3, 4, 5]
calculate_time_complexity(array)
