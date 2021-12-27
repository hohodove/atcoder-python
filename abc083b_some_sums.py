N, A, B = map(int, input().split())

total = 0
for n in range(N+1):
  keta_total = sum(list(map(int, str(n))))
  if A <= keta_total <= B:
    total += n

print(total)
