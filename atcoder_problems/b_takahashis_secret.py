N, X = map(int, input().split())
A = list(map(int, input().split()))

secret = [False]*N

i = X
count = 0

while secret[i-1] == False:
  secret[i-1] = True
  count += 1
  i = A[i-1]

print(count)
