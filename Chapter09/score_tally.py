from icecream import ic


def tally():
    score = 0
    while True:
        increment = yield score
        if increment is None:
            increment = 0
        score += increment


if __name__ == '__main__':
    enthroners = tally()
    sharks = tally()
    ic(next(enthroners))
    ic(next(sharks))
    ic(next(enthroners))
    ic(next(sharks))
    ic(enthroners.send(20))
    ic(sharks.send(10))
    ic(enthroners.send(15))
    ic(sharks.send(20))
    ic(next(enthroners))
    ic(next(sharks))
