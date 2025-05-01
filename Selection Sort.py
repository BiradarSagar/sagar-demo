def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

user_input = input("Enter numbers separated by spaces: ")
# Convert input string to list of integers
arr = list(map(int, user_input.split()))

print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)

#Time O(n2) Space O(1)
