# def findKthMissing(arr, k):
#     if not arr or k <= 0:
#         raise Exception("Invalid input")
    
#     if k < arr[0]:
#         return k

#     missing_count = 0
#     num_tracker = 1

#     while missing_count < k:
#         if num_tracker not in arr:
#             missing_count += 1
#         num_tracker += 1

#     return num_tracker - 1



def kth_missing_positive_number(arr, k):
    if not arr or k < 0:
        raise Exception("Invalid input")
    
    if k < arr[0]:
        return k
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing_count = arr[mid] - mid - 1

        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


