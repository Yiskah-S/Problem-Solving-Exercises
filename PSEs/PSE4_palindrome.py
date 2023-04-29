def palindrome(s):
    if isinstance(s, dict) or not s:
        raise TypeError("Invalid input")

    if not isinstance(s, str):
        test_string = str(s)

    test_string = ''.join(filter(str.isalnum, s.lower()))
    return test_string == test_string[::-1]