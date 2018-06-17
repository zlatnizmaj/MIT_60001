grades = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
for s in grades: # print all keys of dictionary 'grades'

    print("key '{}' have value: {}".format(s, grades[s]))
L = grades.values()
print(len(L))
print(grades.keys())

print(L)
