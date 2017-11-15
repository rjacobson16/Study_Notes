#reverse a string recursively

def reverse(s):
    if len(s) == 1:
        return s[0];

    return s[-1] + reverse(s[:-1])


print(reverse('hello world'))

#find all permutations of a string

def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i,let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                print('perm is ', perm)
                out+=[let+perm]


    return out

print(permute('abcd'))


def fibs_dynamic(n):
    cache = {}
    if n <= 1:
        return 0

    if n == 2:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = fibs_dynamic(n-1) + fibs_dynamic(n-2)

    return cache[n]

print(fibs_dynamic(8))
