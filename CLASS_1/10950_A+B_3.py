T = int(input())
X_list = []
Y_list = []
for i in range(T):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)
for i in range(T):
    print(X_list[i] + Y_list[i])