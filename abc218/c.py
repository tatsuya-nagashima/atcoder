N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def rotate(S):
    res = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[i][j] = S[j][N-1-i]
    return res 

def is_same(s, t):
    s_min_i = N
    s_min_j = N
    t_min_i = N
    t_min_j = N

    ok = True
    for i in range(N):
        for j in range(N):
            if s[i][j] == '#':
                s_min_i = min(s_min_i, i)
                s_min_j = min(s_min_j, j)
            if t[i][j] == '#':
                t_min_i = min(t_min_i, i)
                t_min_j = min(t_min_j, j)    

    for i in range(N):
        for j in range(N):
            si = s_min_i + i  
            sj = s_min_j + j   
            if si < N and sj < N:
                schar = s[si][sj]
            else:
                schar = '.'

            ti = t_min_i + i  
            tj = t_min_j + j   
            if ti < N and tj < N:
                tchar = t[ti][tj]
            else:
                tchar = '.'

            if schar != tchar:
                ok = False

    return ok

ok = False
ok |= is_same(S, T)
S = rotate(S)
ok |= is_same(S, T)
S = rotate(S)
ok |= is_same(S, T)
S = rotate(S)
ok |= is_same(S, T)
S = rotate(S)

if ok: print('Yes')
else: print('No')

