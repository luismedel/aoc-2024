
from io import TextIOWrapper


def parse_orders(f: TextIOWrapper) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    while True:
        line = f.readline().strip()
        if not line:
            break
        left, right = (int(s) for s in line.split("|"))
        pages = result.get(left)
        if not pages:
            pages = []
            result[left] = pages
        pages.append(right)
    return result

def parse_prints(f: TextIOWrapper) -> list[int]:
    result: list[int] = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        result.append(tuple(int(s) for s in line.split(",")))
    return result

def is_ordered(orders: dict[int, int], pages: list[int]) -> bool:
    prev = pages[0]
    for i in range(1, len(pages)):
        if prev not in orders:
            return False
        if pages[i] not in orders[prev]:
            return False
        prev = pages[i]
    return True

orders: dict[int, int]
prints: list[int]

with open("input.txt", "r") as file:
    orders = parse_orders(file)
    prints = parse_prints(file)

sum: int = 0

for i in range(len(prints)):
    if is_ordered(orders, prints[i]):
        middle = prints[i][len(prints[i]) // 2]
        sum += middle

print(sum)
