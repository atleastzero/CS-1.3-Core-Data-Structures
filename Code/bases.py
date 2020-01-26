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

    total = 0
    if "." in digits:
        whole, fraction = digits.split(".", 1)
    else:
        whole = digits
        fraction = "0"
    for pos, digit in enumerate(whole[::-1]):
        number = numberOf(digit)
        number *= (base ** pos)
        total += number
    for pos, digit in enumerate(fraction):
        number = numberOf(digit)
        number *= (base ** (-1 * (pos + 1)))
        total += number

    return total

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    numLeft = number
    oldPos = 1
    posVal = 1
    result = ''
    while numLeft >= 1:
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

    if result == "":
        result = "0"

    if numLeft > 0:
        result += "."

    digits = 0
    while numLeft > 0 and digits < 5:

        whole = int(numLeft * base)
        result += numberTo(whole, base)
        numLeft = numLeft * base - whole
        digits += 1

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

def encodeTwosComplement(number, bits):
    negative = False
    absoluteValue = number
    if number < 0:
        negative = True
        absoluteValue = -1 * number

    binary = encode(absoluteValue, 2)

    length = len(binary)
    for _ in range(bits - length):
        binary = "0" + binary

    if not negative:
        return binary


    onesComplement = ""
    for digit in binary:
        if digit == "1":
            onesComplement += "0"
        else:
            onesComplement += "1"

    return addOneBinary(onesComplement)

def addOneBinary(digits):
    result = ""
    for digit in digits[::-1]:
        if digit == "0":
            result = '1' + result
            return digits[:len(digits) - len(result)] + result
        else:
            result = '0' + result
    return result

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
    print(encodeTwosComplement(10, 8))
    print(encodeTwosComplement(-10, 8))