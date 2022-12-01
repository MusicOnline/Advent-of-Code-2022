top_three_calories: list[int] = [0, 0, 0]  # Highest to lowest
last_calories: int = 0


def insert_if_higher(calories: int) -> None:
    for i, top_calories in enumerate(top_three_calories):
        if calories > top_calories:
            top_three_calories.pop()
            top_three_calories.insert(i, calories)
            return


with open("input/day-1.txt") as f:
    line = f.readline()
    while line:
        if line == "\n":
            insert_if_higher(last_calories)
            last_calories = 0
        else:
            last_calories += int(line[:-1])
        line = f.readline()

insert_if_higher(last_calories)
print(sum(top_three_calories))
