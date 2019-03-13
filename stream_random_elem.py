# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random

theStream = ["Andrew", "Dora", "Paul", "Jessica", "Lavinia", "Alicia", "Piper"]


def pick(big_stream):
    random_element = None

    for (i, e) in enumerate(theStream):
        if random.randint(0, i) == 0:
            random_element = e

    return random_element


print(pick(theStream))
