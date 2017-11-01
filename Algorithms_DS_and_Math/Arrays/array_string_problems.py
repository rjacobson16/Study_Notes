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
