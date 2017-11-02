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

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    max_so_far = arr[0]
    max_ending_here = 0
    max_element = arr[0]
    start_idx = end_idx = current_idx = 0

    for i, v in enumerate(arr):
        if v > max_element:
            max_element = v
            max_idx = i

        max_ending_here += v
        if max_ending_here < 0:
           max_ending_here = 0
           current_idx = i+1

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start_idx = current_idx
            end_idx = i

    if max_so_far > 0:
        return f"The largest continuous subarray is {arr[start_idx:end_idx]}, which sums to {max_so_far}"
    else:
        return f"All Neg: The largest continuous subarray is {[arr[max_idx]]}, which sums to {max_element}"
