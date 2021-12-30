import math

X, Y = map(int, input().split())

if X >= Y:
  print(0) 
  exit()

husoku = Y - X

print(math.ceil(husoku/10))
