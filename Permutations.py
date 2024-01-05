n = int(input())
if n > 4 or n == 1:
    lst_even = [str(x) for x in range(1, n + 1, 2)]
    lst_odd = [str(x) for x in range(2, n + 1, 2)]
    print(" ".join((lst_even + lst_odd)))
elif n == 4:
    print("3 1 4 2")
else:
    print("NO SOLUTION")
