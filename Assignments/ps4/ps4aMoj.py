def get_permutation(s, i):

    for j in range(i, len(s)):
        if i == len(s) - 1:
            print(s)
        else:
            s[i], s[j] = s[j], s[i]
            get_permutation(s, i+1)
            s[i], s[j] = s[j], s[i]


get_permutation([1,2], 0)
