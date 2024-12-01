import re


left = []
right = []

with open("input.txt") as file:
    for line in file:
        a, b = re.split(r'\s+', line.strip(), maxsplit=1)
        left.append(int(a))
        right.append(int(b))

left = sorted(left)
right = sorted(right)

print(sum(abs(a - b) for a, b in zip(left, right)))
