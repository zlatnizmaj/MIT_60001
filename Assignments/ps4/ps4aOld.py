# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
from scipy.signal import firls


def get_permutations(sequence):
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
    def toString(s):
        return ''.join(s)

    def permutation(s, i):
        if i == len(s) - 1:
            print(toString(s))
        else:
            for index in range (i, len(s)):
                s[i], s[index] = s[index], s[i] # swap hai gia tri tai i va index
                permutation(s, i + 1)
                s[i], s[index] = s[index], s[i]

    s = list(sequence)
    permutation(s, 0) # bat dau tu vi tri dau tien cua list (index = 0)

if __name__ == '__main__':

    example_input = 'abc'
    print("Input:", example_input)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:")
    get_permutations(example_input)

    example_input = str(input("Enter a string for permutation: ")) # nhap day can tim to hop
    # tinh so to hop se xuat ra
    number_of_permutation = 1
    for i in range (1, len(example_input)+1):
        number_of_permutation *= i
    print("Number of permutation = {}".format(number_of_permutation))
    # cac to hop cua day vua nhap
    get_permutations(example_input)
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



