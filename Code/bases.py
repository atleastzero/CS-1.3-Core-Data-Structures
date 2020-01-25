#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# convert a character number or letter to a number
def numberOf(number):
    """Find the numerical equivalent of a given alphanumeric character
    number: str -- string representation of a number in some base 2-36
    return: int -- integer representation of the number in decimal"""
    assert number in string.digits or number in string.ascii_letters, 'character {} is not a number'.format(number)
    if number in string.ascii_letters:
        return string.ascii_letters.index(number) % 26 + 10
    else:
        return int(number)

def numberTo(number, base):
    if number < 10:
        return str(number)
    else: 
        return string.ascii_lowercase[number - 10]

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    sum = 0
    whole, fraction = digits.split(".", 1)
    for pos, digit in enumerate(whole[::-1]):
        number = numberOf(digit)
        number *= (base ** pos)
        sum += number
    for pos, digit in enumerate(fraction):
        number = numberOf(digit)
        number *= (base ** (-1 * (pos + 1)))
        sum += number

    return sum

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # PSEUDO:
    #   while number left > 0
    #       while position value * base < number left
    #           increase position, posval
    #       digit gets numleft / posval, truncated
    #       numleft becomes remainder of above
    #   fill in 0s for remaining positions
    numLeft = number
    oldPos = 1
    posVal = 1
    result = ''
    while numLeft > 0:
        newPos = 1
        while posVal * base <= numLeft:
            posVal *= base
            newPos += 1
        while newPos < oldPos - 1:
            result += '0'
            oldPos -= 1
        result += numberTo(int(numLeft / posVal), base)
        numLeft %= posVal
        posVal = 1
        oldPos = newPos
    for _ in range(1, oldPos):
        result += "0"
    return result

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    inDecimal = decode(digits, base1)
    return encode(inDecimal, base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    # main()
    print(decodeWithRadix("1101.101", 2))