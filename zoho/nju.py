T = int(input())
for t in range(T):
    line = input()
    #M, N, P = list([int(x) for x in line.split()])
    M, N, P=line.split()
    M=int(M)
    N=int(N)
    P=int(P)
    maxs = [0] * N
    john = None
    for m in range(1, M + 1):
        line = input()
        steps = [int(x) for x in line.split()]
        print(steps,maxs)
        for i in range(N):
            if steps[i] > maxs[i]:
                maxs[i] = steps[i]
        if m == P:
            john = steps
    additional = 0
    for i in range(N):
        additional += max(0, maxs[i] - john[i])
    print("Case #%d: %d" % (t+1, additional))