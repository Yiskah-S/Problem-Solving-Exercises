6list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]

def merge_lists(list1, list2):
    if not (list1 or list2):
        raise ValueError("Both lists are empty")
    
    if not all(isinstance(lst, list) for lst in (list1, list2)):
        raise TypeError("Invalid input, lists must be a list")

    for num in list1 + list2:
        if not isinstance(num, (int, float)):
            raise TypeError("Invalid input in list")
        
    # list1 = list(filter(lambda num: num not in list2, list1))
    if len(set(list1 + list2)) != len(list1 + list2):
        duplicates = set()
        for num1 in list1:
            for num2 in list2:
                if num1 == num2:
                    duplicates.add(num1)
                    break
        for num in list1:
            if num in duplicates:
                list1.remove(num)

    if not list1:
        return list2
    elif not list2:
        return list1
    elif list1[0] < list2[0]:
        return [list1[0]] + merge_lists(list1[1:], list2)
    else:
        return [list2[0]] + merge_lists(list1, list2[1:])

test = merge_lists(list1, list2)
print(f"{test = }")