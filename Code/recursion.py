#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    answer = n
    if n == 0:
        answer = 1
    for number in range(n):
        if number > 1:
            answer *= number
    return answer


def factorial_recursive(n):
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)

permutation_lookup_table = {}

def permutations(arr, n=-1):
    all_perms = []
    string = False
    if n < 1:
        n = len(arr)
    if isinstance(arr, str):
        string = True
    if n == 1:
        all_perms.append(arr)
    else:
        for i in range(n):
            if (arr, n-1) in permutation_lookup_table:
                new_additions = permutation_lookup_table[(arr, n-1)]
            else:
                new_additions = permutations(arr, n-1)
            for narr in new_additions:
                all_perms.append(narr)
            arr = list(arr) 
            if n % 2 == 0:
                # swap elements 0 and n-1
                arr[0], arr[n-1] = arr[n-1], arr[0]
            else: 
                # swap elements i and n-1
                arr[i], arr[n-1] = arr[n-1], arr[i]
            if string:
                arr = "".join(arr)

    permutation_lookup_table[(arr, n)] = all_perms
    return all_perms

combonation_lookup_table = {}

def combinations(n, arr):
    all_combs = []
    if n == 1:
        for val in arr:
            all_combs.append(val)
    else:
        for i, val in enumerate(arr):
            for j in combinations(n-1, arr[i+1:]):
                all_combs.append("" + val + j)
    return all_combs

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))

if __name__ == '__main__':
    # main()
    print(permutations("1234"))
    # print(combinations(3, "1234"))
