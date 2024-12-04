
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
    if get_char(row, col) != "X" and get_char(row, col) != "S":
        return 0

    def check_word(word: str, rdir: int, cdir: int) -> bool:
        row_ = row
        col_ = col
        for c in word:
            if get_char(row_, col_) != c:
                return False
            row_ += rdir
            col_ += cdir
        return True

    count: int = 0

    for word in ("XMAS", "SAMX"):
        if check_word(word, 1, 0):
            count += 1

        if check_word(word, 0, 1):
            count += 1

        if check_word(word, 1, 1):
            count += 1

        if check_word(word, 1, -1):
            count += 1
    return count


count: int = 0
for row in range(ROWS):
    for col in range(COLS):
        count += count_xmas(row, col)

print(count)