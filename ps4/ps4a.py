"""
@subject:
Bài tập giữa kì môn Giải thuật nâng cao
Assignments MIT6_0001
ps4a.py

@author:
Nguyễn Phương Nam
Lớp KHMT_ĐHSP_ K28

"""
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
    if len(sequence) <= 1:
        return [sequence] # buoc dung de quy

    output_list_all_permutations = []  # return list as result of function

    for letter in sequence:
        permutations = get_permutations(sequence.replace(letter, '', 1)) # buoc de quy, voi string moi bo di ky tu dau tien
        for perm in permutations: # list permutations
            newperm = letter + perm
            if output_list_all_permutations.count(newperm) == 0: # kiem tra chuoi da ton tai trong list chua
                output_list_all_permutations.append(letter + perm) # neu chua thi add vao list

    return output_list_all_permutations

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



