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
    """Return a boolean indicating whether pattern occurs in text.
    Best case running time: O(p) because must be traversed to at 
    least pattern length
    Worst case running time: O(t*p) because in case of all fake starts with no
    or last match, must traverse pattern length for each letter in t"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
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
    or None if not found.
    Best case running time: O(p) because must be traversed to at 
    least pattern length
    Worst case running time: O(t*p) because in case of all fake starts with no
    or last match, must traverse pattern length for each letter in t"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if len(pattern) == 0:
        return 0
    i = find_next_possible_start(text, pattern, 0)
    while i is not None:
        if is_match(text, pattern, i):
            return i
        i = find_next_possible_start(text, pattern, i+1)

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Best case and worst case running time: O((t-p)*p) because must traverse t-p 
    for all possible starts and each p times"""
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

def is_anagram(word1, word2):
    if len(word1) == 1 and word1 == word2:
        return True
    for letter in word1:
        try:
            two_index = word2.index(letter)
            return is_anagram(word1[1:], word2[: two_index] + word2 [two_index+1:])
        except:
            return False

def anagrams(text):
    f = open("/usr/share/dict/words", "r")
    contents = f.read()
    words_list = contents.split("\n")
    f.close()
    anagram_list = []
    for word in words_list:
        if len(text) == len(word) and text != word:
            if is_anagram(text, word):
                anagram_list.append(word)
    return anagram_list

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
