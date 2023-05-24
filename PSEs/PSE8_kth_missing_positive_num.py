arr = [2, 3, 4, 7, 11]
k = 5

def kth_missing_positive_number(arr, k):
    if not arr or k < 0:
        raise Exception("Invalid input")
    
    if k < arr[0]:
        return k

    missing_num_counter = 0
    missing_num_tracker = 0

    while missing_num_counter != k:
        missing_num_tracker += 1
        if missing_num_tracker not in arr:
            missing_num_counter += 1

    return missing_num_tracker

