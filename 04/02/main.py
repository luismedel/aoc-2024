
input_: list[str]

with open("input.txt") as file:
    input_ = file.readlines()

COLS = len(input_[0])
ROWS = len(input_)


def get_char(row: int, col: int) -> str:
    if row < 0 or col < 0 or row >= ROWS or col >= COLS:
        return ""
    return input_[row][col]

def count_xmas(row: int, col: int) -> int:
    if get_char(row, col) != "A":
        return 0

    diag1 = (get_char(row - 1, col - 1) == "M" and get_char(row + 1, col + 1) == "S") or (get_char(row - 1, col - 1) == "S" and get_char(row + 1, col + 1) == "M")
    diag2 = (get_char(row - 1, col + 1) == "M" and get_char(row + 1, col - 1) == "S") or (get_char(row - 1, col + 1) == "S" and get_char(row + 1, col - 1) == "M")
    if diag1 and diag2:
        return 1

    return 0


count: int = 0
for row in range(ROWS):
    for col in range(COLS):
        count += count_xmas(row, col)

print(count)