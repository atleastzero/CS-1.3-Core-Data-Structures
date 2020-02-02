#!python

def find_next_possible_start(text, pattern, index):
    for i in range(index, len(text) - len(pattern) + 1):
        if text[i] == pattern[0]:
            return i
    return None

def is_match(text, pattern, index):
    for j in range(len(pattern)):
        if text[index + j] != pattern[j]:
            return False
    return True

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if len(pattern) == 0:
        return True
    i = find_next_possible_start(text, pattern, 0)
    while i is not None:
        if is_match(text, pattern, i):
            return True
        i = find_next_possible_start(text, pattern, i+1)
    
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if len(pattern) == 0:
        return 0
    # i = find_next_possible_start(text, pattern, 0)
    # while i is not None and i < len(text):
    #     j = 0
    #     matching = True
    #     while j < len(pattern) and matching:
    #         if text[i + j] != pattern[j]:
    #             matching = False
    #         j += 1
    #     if matching:
    #         return i
    #     i = find_next_possible_start(text, pattern, i+1)
    i = find_next_possible_start(text, pattern, 0)
    while i is not None:
        if is_match(text, pattern, i):
            return i
        i = find_next_possible_start(text, pattern, i+1)

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    starts = []

    if len(pattern) == 0:
        for i in range(len(text)):
            starts.append(i)
    else:
        i = find_next_possible_start(text, pattern, 0)
        while i is not None:
            if is_match(text, pattern, i):
                starts.append(i)
            i = find_next_possible_start(text, pattern, i+1)
    return starts

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
