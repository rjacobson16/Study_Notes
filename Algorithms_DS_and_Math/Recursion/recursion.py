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

def rec_coin_no_memo(target, coins):

    min_coins = target

    if target in coins:
        return 1

    else:

        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin_no_memo(target-i, coins)

            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

#print(rec_coin_no_memo(63, [1,5,10,25]))

def rec_coin_w_memo(target, coins, known):

    min_coins = target

    if target in coins:
        known[target] = 1
        return 1

    elif known[target] > 0:
        return known[target]

    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_w_memo(target-i, coins, known)

            print ('Num coins: ', num_coins, 'target: ', target-i)

            if num_coins < min_coins:
                min_coins = num_coins
                known[target] = min_coins

    return min_coins

print(rec_coin_w_memo(63, [1,5,10,25], [0]*(63+1)))
