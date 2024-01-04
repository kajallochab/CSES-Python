limit = int(input())
number_set = set(map(int, input().split()))
expected_set = set([x for x in range(1, limit + 1)])
print((list(expected_set - number_set))[0])
