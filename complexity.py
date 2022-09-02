n = input()
n = int(n)

count = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
# O(n^3)
# n = 5
# = O(5^3)
# = 125

print("n =", n, "count =", count)
