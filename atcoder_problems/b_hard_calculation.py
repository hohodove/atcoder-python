A, B = input().split()

A = A[::-1]
B = B[::-1]

if len(A) <= len(B):
  keta = len(A)
else:
  keta = len(B)

for i in range(keta):
  if (int(A[i]) + int(B[i])) > 9:
    print("Hard")
    exit(0)

print("Easy")
