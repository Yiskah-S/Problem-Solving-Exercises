def hamming_distance(strand1, strand2):
    if not isinstance(strand1, str) or not isinstance(strand2, str):
        raise ValueError("Both strands must be strings.")
    if not strand1 or not strand2:
        raise ValueError("Strands cannot be empty.")
    if len(strand1) != len(strand2):
        raise ValueError("Strands must be of equal length.")
    counter = 0
    for i in range(len(strand1)):
        if strand1[i] != strand2[i]:
            counter += 1
    return counter