import sys

S = input()
S = S[::-1]

t = ["dream", "dreamer", "erase", "eraser"]
t2 = []

for t1 in t:
  t2.append(t1[::-1])

T = ""

while not (T == S):
  umu = len(T)
  for i in t2:
    if S[len(T):(len(T)+len(i))] == i:
      T += i
  if len(T) == umu:
    print("NO")
    sys.exit()

print("YES")
