import re


offset = 0
input_ = []
mul_enabled = True


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


def peek() -> str:
    if offset >= len(input_):
        return ""
    return input_[offset]


def unget() -> None:
    global offset
    offset -= 1


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
    for expected in "mul":
        if get_next() != expected:
            unget()
            return 0

    if get_next() != "(":
        unget()
        return 0
    
    a = consume_num()
    if a == "":
        return 0

    if get_next() != ",":
        unget()
        return 0

    b = consume_num()
    if b == "":
        return 0

    if get_next() != ")":
        unget()
        return 0

    return int(a) * int(b)


def consume_conditional() -> None:
    global mul_enabled
    
    for expected in "do":
        if get_next() != expected:
            unget()
            return False

    is_do = True

    if get_next() != "(":
        unget()
        for expected in "n't":
            if get_next() != expected:
                unget()
                return False

        if get_next() != "(":
            unget()
            return False

        is_do = False

    if get_next() != ")":
        unget()
        return False

    mul_enabled = is_do


with open("input.txt") as file:
    input_ = file.read().strip()

sum_ = 0
while True:
    try:
        if peek() == "d":
            consume_conditional()
        elif peek() == "m":
            v = consume_mul()
            if v and mul_enabled:
                sum_ += v
        else:
            get_next()
    except EOF:
        break

print(sum_)
