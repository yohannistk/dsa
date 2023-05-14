
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binary_search(arr : list[int], target : int):
    first_index = 0
    last_index = len(arr) - 1
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] > target:
            last_index = mid_index - 1
        elif arr[mid_index] < target:
            first_index = mid_index + 1
    return -1

print(binary_search(nums, 1))
