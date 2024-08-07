import random


class Door:
    def __init__(self, num, correct, picked):
        self.num = num
        self.correct = correct
        self.picked = picked


def create_random_doors():
    values = [True, False, False]

    random.shuffle(values)

    d1 = Door(1, values[0], False)
    d2 = Door(2, values[1], False)
    d3 = Door(3, values[2], False)

    return d1, d2, d3


def pick_door(rd1, rd2, rd3):
    rd_list = [rd1, rd2, rd3]
    picked_door = random.choice(rd_list)
    picked_door.picked = True
    return picked_door.num


def discard_door(upd1, upd2, upd3):
    upd_list = []

    for upd in [upd1, upd2, upd3]:
        if upd.picked:
            continue
        else:
            upd_list.append(upd)

    remaining_d = random.choice(upd_list)

    if remaining_d.correct:
        return remaining_d.num
    else:
        if upd_list[0].correct:
            return upd_list[0].num
        else:
            return upd_list[1].num


def get_door_by_num(num, d1, d2, d3):
    for d in [d1, d2, d3]:
        if d.num == num:
            return d
    return None


def play(stay=True):
    door1, door2, door3 = create_random_doors()
    picked_door_num = pick_door(door1, door2, door3)

    remaining_door_num = discard_door(door1, door2, door3)


    if stay:
        return get_door_by_num(picked_door_num, door1, door2, door3).correct
    else:
        return get_door_by_num(remaining_door_num, door1, door2, door3).correct


def main():
    stay_wins = 0
    switch_wins = 0
    for _ in range(100):
        if play(stay=True):
            stay_wins += 1

        if play(stay=False):
            switch_wins += 1

    print(f"stay won {stay_wins} times out of 100 with win probability {stay_wins / 100 * 100}%")
    print(f"switch won {switch_wins} times out of 100 with win probability {switch_wins / 100 * 100}%")


if __name__ == '__main__':
    main()
