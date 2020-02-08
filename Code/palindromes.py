#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    """Best and worst case running time: O(n) because must be traversed to at 
    least halfway through the list"""
    front = 0
    back = len(text) - 1
    while front < back:
        while not text[front].isalpha() and front < back:
            front += 1
        while not text[back].isalpha() and front < back:
            back -= 1
        if front < back and text[front].lower() != text[back].lower():
            return False
        front += 1
        back -= 1
    return True

def is_palindrome_recursive(text):
    """Best and worst case running time: O(n) because must be traversed to at 
    least halfway through the list"""
    if len(text) <= 1:
        return True
    
    while len(text) > 0 and not text[0].isalpha():
        text = text[1:]
    while len(text) > 0 and not text[len(text)-1].isalpha():
        text = text[:len(text)-1]

    if text[0].lower() != text[len(text)-1].lower():
        return False
    else:
        text = text[1:len(text)-1]

    while len(text) > 0 and not text[0].isalpha():
        text = text[1:]
    while len(text) > 0 and not text[len(text)-1].isalpha():
        text = text[:len(text)-1]

    return is_palindrome_recursive(text)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    is_palindrome_recursive("No, On!")
