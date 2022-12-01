highest_calories: int = 0
last_calories: int = 0


def swap_if_higher(calories: int) -> None:
    global highest_calories
    if calories > highest_calories:
        highest_calories = calories


with open("input/day-1.txt") as f:
    line = f.readline()
    while line:
        if line == "\n":
            swap_if_higher(last_calories)
            last_calories = 0
        else:
            last_calories += int(line[:-1])
        line = f.readline()

swap_if_higher(last_calories)
print(highest_calories)
