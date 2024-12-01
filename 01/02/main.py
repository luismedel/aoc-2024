import re


left = set()
right = []

with open("input.txt") as file:
    for line in file:
        a, b = re.split(r'\s+', line.strip(), maxsplit=1)
        left.add(int(a))
        right.append(int(b))

print(sum(n * sum(1 if m == n else 0 for m in right) for n in left))
