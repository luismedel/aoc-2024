
import copy
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

def reorder(orders: dict[int, int], pages: list[int]) -> list[int]:
    pages = copy.copy(pages)
    while True:
        result: list[int] = []

        needs_reorder = False

        curr: int = pages[0]
        next: int
        
        for i in range(1, len(pages)):
            next = pages[i]
            if (curr in orders) and (next in orders[curr]):
                result.append(curr)
                curr = next
            else:
                result.append(next)
                needs_reorder = True

        if needs_reorder:
            result.append(curr)
            pages = result
        else:
            return result

orders: dict[int, int]
prints: list[int]

with open("input.txt", "r") as file:
    orders = parse_orders(file)
    prints = parse_prints(file)

sum: int = 0

for i in range(len(prints)):
    if not is_ordered(orders, prints[i]):
        ordered = reorder(orders, prints[i])
        middle = ordered[len(ordered) // 2]
        sum += middle

print(sum)
