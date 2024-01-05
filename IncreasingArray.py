n = int(input())
number_lst = list(map(int, input().split()))
moves = 0
for index in range(n - 1):
    if number_lst[index + 1] < number_lst[index]:
        moves += number_lst[index] - number_lst[index + 1]
        # print(index)
        # print("moves = ", moves)
        number_lst[index + 1] = number_lst[index]
    else:
        continue
print(moves)
