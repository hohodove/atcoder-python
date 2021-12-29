S = input()
T = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(S)):
  k = alphabet.index(T[i]) - alphabet.index(S[i])

  if k >= 0:
    pass
  else:
    k = 26 + k

  if i == 0:
    K = k

  if K == k:
    pass
  else:
    print("No")
    exit(0)

print("Yes")
