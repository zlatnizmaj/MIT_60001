L_mixed = [2, 'a', 4, [1, 2]]
L = [2, 1, 3]

# iterating over a list
# sum of all element type integer in List L
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += i
print(total)

# add elements to end of list with append(element)
L.append(5)
print(L)
L_mixed.append("MrGao")
print(L_mixed)
L_concatenation = L + L_mixed
print(L_concatenation)

# extend(some_list) # extend with other list, such concatenation
L.extend([4, 6])
print(L)
# remove element
L_will_removed_ele = [2, 1, 3, 6, 3, 7, 0]
print(L_will_removed_ele)

L_will_removed_ele.remove(2)
print(L_will_removed_ele)

L_will_removed_ele.remove(3)
print(L_will_removed_ele)

del(L_will_removed_ele[1])
print(L_will_removed_ele)

print(L_will_removed_ele.pop())
print(L_will_removed_ele)

# convert list to strings and back
# convert list to string: list(s)
# s.split(): split a string on a character on spaces

s = str(input("Enter your full name: "))
# L_from_string = list(s)
# print(L_from_string)
L_with_split_spaces = s.split()
print(L_with_split_spaces)
for char in L_with_split_spaces:
    print(char)

L_to_string = ['a', 'b', 'c']
print(''.join(L_to_string))
print('_'.join(L_to_string))
print(s)
#L_copy = L_from_string[:]
# L_copy.append(" Pooh U")
# print(L_from_string)
# print(L_copy)
# print(list(''.join(L_copy)))
