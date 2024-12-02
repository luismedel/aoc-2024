import re


reports = []

with open("input.txt") as file:
    reports.extend(list((int(v) for v in line.strip().split(" "))) for line in file)

def delta(i: int, report: list[int]) -> int:
    return report[i] - report[i - 1]

def valid_step(delta: int) -> bool:
    return abs(delta) >= 1 and abs(delta) <= 3

def get_deltas(report: list[int]) -> list[int]:
    return list(delta(i + 1, report) for i in range(len(report) - 1))

def valid_report(report: list[int]) -> bool:
    deltas = get_deltas(report)
    if deltas[0] > 0:
        return all(d > 0 and valid_step(d) for d in deltas)
    else:
        return all(d < 0 and valid_step(d) for d in deltas)

count = 0
for report in reports:
    if valid_report(report):
        count += 1
        continue

    # Brute force ftw
    for i in range(len(report)):
        if valid_report(report[:i] + report[i+1:]):
            count += 1
            break

print(count)
