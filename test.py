N, A, B = map(int, input().split())

total = 0
for n in range(N+1):
  keta_list = list(map(int, [str(n)[s] for s in range(len(str(n)))]))
  keta_total = sum(keta_list)
  if A <= keta_total <= B:
    total += n

print(total)
