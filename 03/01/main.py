import re


offset = 0
input_ = []


class EOF(Exception):
    pass


def get_next() -> str:
    global input_
    global offset

    if offset >= len(input_):
        raise EOF()
    result = input_[offset]
    offset += 1
    return result


def unget() -> None:
    global offset
    offset -= 1


def skip() -> None:
    c = get_next()
    while not re.match(r"[a-z]", c):
        c = get_next()
    unget()


def consume_num() -> str:
    n = ""
    for _ in range(3):
        c = get_next()
        if not c.isdigit():
            unget()
            break
        n += c
    return n


def consume_mul() -> int:
    skip()
    
    for expected in ("m", "u", "l"):
        if get_next() != expected:
            return 0

    if get_next() != "(":
        return 0
    
    a = consume_num()
    if a == "":
        return 0

    if get_next() != ",":
        return 0

    b = consume_num()
    if b == "":
        return 0

    if get_next() != ")":
        return 0

    return int(a) * int(b)


with open("input.txt") as file:
    input_ = file.read().strip()

sum_ = 0
while True:
    try:
        sum_ += consume_mul()
    except EOF:
        break

print(sum_)
