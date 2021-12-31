import itertools

N, M = map(int, input().split())

himo_a = [[False]*N for _ in range(N)]
himo_c = [[False]*N for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  a += -1
  b += -1
  himo_a[a][b] = himo_a[b][a] = True

for _ in range(M):
  c, d = map(int, input().split())
  c += -1
  d += -1
  himo_c[c][d] = himo_c[d][c] = True

ans = False

for p in itertools.permutations(range(N)):
  ok = True
  for i in range(N):
    for j in range(N):
      if himo_a[i][j] != himo_c[p[i]][p[j]]:
        ok = False
  if ok:
    ans = True
    break

print("Yes" if ans else "No")
