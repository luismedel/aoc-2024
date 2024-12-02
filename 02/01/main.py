import re


reports = []

with open("input.txt") as file:
    reports.extend(list((int(v) for v in line.strip().split(" "))) for line in file)

def delta(i: int, report: list[int]) -> int:
    return report[i] - report[i - 1]

def valid_step(delta: int) -> bool:
    return abs(delta) >= 1 and abs(delta) <= 3

count = 0
for report in reports:
    deltas = (delta(i + 1, report) for i in range(len(report) - 1))
    if delta(1, report) > 0:
        if all(d > 0 and valid_step(d) for d in deltas):
            count += 1
    else:
        if all(d < 0 and valid_step(d) for d in deltas):
            count += 1

print(count)