N, A, B = map(int, input().split())

total = 0
for n in range(N+1):
  sum = sum(map(int, [n[s] for s in range(len(str(n)))]))
  if A <= sum <= B:
    total += sum

print(total)
