# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
from scipy.signal import firls


def get_permutations(mystr):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    #>>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    :rtype: object
    '''
    if len(mystr) <= 1:
        return [mystr]
    res = []
    for elt in mystr:
        permutations = get_permutations(mystr.replace(elt, ""))
        for permutation in permutations:
            res.append(elt + permutation)
    return res

if __name__ == '__main__':

    example_input = 'abc'
    print("Input:", example_input)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:")
    print(get_permutations(example_input))

    example_input = str(input("Enter a string for permutation: ")) # nhap day can tim to hop
    # tinh so to hop se xuat ra
    number_of_permutation = 1
    for i in range (1, len(example_input)+1):
        number_of_permutation *= i
    print("Number of permutation = {}".format(number_of_permutation))
    # cac to hop cua day vua nhap
    print(get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



