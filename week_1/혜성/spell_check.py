# A. Spell Check

import sys

name = {"T", "i", "m", "u", "r"}
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    check = set(sys.stdin.readline().split()[0])
    if n != len(name):
        print("NO")
    elif len(name.symmetric_difference(check)) == 0:
        print("YES")
    else:
        print("NO")
