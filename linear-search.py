def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 9
result = linear_search(nums, target)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")
