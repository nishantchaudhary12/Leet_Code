'''Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.'''


def toLowerCase(self, str):
    """
    :type str: str
    :rtype: str
    """
    new_str = ''
    for each in str:
        ascii_val = ord(each)
        if ascii_val < 97 and each.isalpha():
            new_str += chr(ascii_val + 32)
        else:
            new_str += each
    return new_str