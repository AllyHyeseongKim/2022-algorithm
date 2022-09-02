# B. Colourblindness

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    row = sys.stdin.readline().replace("B", "G")
    check = sys.stdin.readline().replace("B", "G")

    if row == check:
        print("YES")
    else:
        print("NO")
