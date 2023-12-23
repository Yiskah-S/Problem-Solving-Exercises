import heapq

"""
A function that returns the k most frequent elements in a given array.

Parameters:
arr (array): a non-empty array of integers
k (int): number of most frequent integers to return 

Returns:
array[int]: 1D array that that returns the k most frequent elements
"""

def most_frequent_k_elements(arr,k):
    if not arr:
        return []
    
    freq_dict = {}
    
    for num in arr:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
            
    heap = []
    
    for num, freq in freq_dict.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    output = [elem[1] for elem in heap]
    
    output.reverse()
    
    return output