N = int(input())
D = [input() for _ in range(N)]
D = list(map(int, D))
sorted_list = []

bucket = [0]*(max(D)+1)

for l in D:
  bucket[l] += 1

#for i in range(1, max(D)+1):
# sorted_list.extend([i]*bucket[i])

count = 0

for i in bucket:
  if i != 0:
    count += 1

print(count)
