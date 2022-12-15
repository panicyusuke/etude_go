import random
from pprint import pprint

SPEED = 105


def task1():
    return 3


def task2():
    tape_length = random.randint(300, 600)
    time = tape_length / SPEED
    return [time, tape_length]


if __name__ == "__main__":
    task = 3
    worker = 3

    t = task1()

    god = dict()
    for worker in range(10):
        god[worker] = {
            "time": [],
            "length": 0
        }
        for n in range(5):
            time_task1 = task1()
            time_task2 = task2()
            total_time = time_task1 + time_task2[0]
            god[worker]["length"] = time_task2[1]
            god[worker]["time"].append(total_time)
    pprint(god)
