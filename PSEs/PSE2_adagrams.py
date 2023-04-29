LETTER_SCORE = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def score(word):
    score = 0
    for letter in word.upper():
        score += LETTER_SCORE.get(letter, 0)
    return score
    

    # total_value = 8 if len(word) >= 7 else 0
    # total_value = 8 * (len(word) >= 7)
    # for letter in word.upper():
    #     total_value += LETTER_SCORE.get(letter, 0)
    # return total_value
    
    