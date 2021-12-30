N = int(input())
S = list(map(int, input().split()))

count = 0
flag = False

for i in range(N):
  flag = False
  for a in range(1,1001):
    for b in range(1, 1001):
      if S[i] == (4*a*b) + 3*(a+b):
        flag = True
  if flag == False:
    count += 1

print(count)
