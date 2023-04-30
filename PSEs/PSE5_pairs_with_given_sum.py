def pairs_with_given_sum(numbers, target):
    if not numbers:
        raise ValueError("Invalid input list")
    if not isinstance(target, (float, int)):
        raise TypeError("Invalid target input")

    num_dict = {}
    pairs = 0
    num_count = 0

    for num in numbers:      
        if isinstance(num, (float, int)):
            num_count += 1
            complement = target - num
            if complement in num_dict and num_dict[complement] > 0:
                pairs += 1
                num_dict[complement] -= 1
            else:
                num_dict[num] = num_dict.get(num, 0) + 1
    if num_count == 0:
            raise ValueError("List contains no numbers")
    elif num_count < 2:
            raise ValueError("List contains insufficient numbers to make pairs")
    return pairs

    