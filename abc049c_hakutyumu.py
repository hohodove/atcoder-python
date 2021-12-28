S = input()
S = S[::-1]

t = ["dream", "dreamer", "erase", "eraser"]
t2 = []

for t1 in t:
  t2.append(t1[::-1])

T = []

while len(T) < len(S):
  for i in t2:
    if S[:len(i)] == i:
      T += i

print("YES") if T == S else print("NO")
