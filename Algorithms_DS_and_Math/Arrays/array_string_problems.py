## Write a method to test whether two strings are anagrams
from collections import Counter

def anagram(str1, str2):
    str1_count, str2_count = Counter(), Counter()

    for c in str1:
        if c == ' ':
            continue

        str1_count[c] +=1

    for c in str2:
        if c == ' ':
            continue

        str2_count[c] +=1

    return str1_count == str2_count

def missing_member(arr1, arr2):
    arr1_count, arr2_count = Counter(), Counter()

    for num in arr1:

        arr1_count[num] +=1

    for num in arr2:

        arr2_count[num] +=1

    for k,v in arr1_count.items():
        if not arr2_count[k] == arr1_count[k]:
            return k

    return None
