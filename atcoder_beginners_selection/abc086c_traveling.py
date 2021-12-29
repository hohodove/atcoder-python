N = int(input())
T, X, Y = [0]*N, [0]*N, [0]*N

for i in range(N):
  t, x, y = map(int, input().split())
  T[i], X[i], Y[i] = t, x, y

pt, px, py = 0, 0, 0

for i in range(N):
  if abs(T[i]-pt) < abs(X[i]-px) + abs(Y[i]-py):
    print("No")
    exit(0)
  if (T[i] % 2 == 0) & ((X[i]+Y[i]) % 2 == 0):
    pass
  elif (T[i] % 2 == 1) & ((X[i]+Y[i]) % 2 == 1):
    pass
  else:
      print("No")
      exit(0)
  pt, px, py = T[i], X[i], Y[i] 

print("Yes")
