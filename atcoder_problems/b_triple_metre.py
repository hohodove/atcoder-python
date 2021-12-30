S = input()
T = "oxxoxxoxxoxx"

for i in range(len(S)+3):
  if T[i:i+len(S)] == S:
    print("Yes")
    exit(0)

print("No")
