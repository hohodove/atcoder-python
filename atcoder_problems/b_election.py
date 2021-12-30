N = int(input())
S = [input() for _ in range(N)]

tousen_num = 0
tousen_name = ""

for i in range(len(S)):
  kouho = S[i]
  cnt = 0
  for j in range(len(S)):
    if S[j] == kouho:
      cnt += 1
  if cnt > tousen_num:
    tousen_num = cnt
    tousen_name = kouho

print(tousen_name)
