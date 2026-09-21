week = 1
while week <= 4:
    points = int(input(f"Week {week} points: "))
    if points >= 100:
        week += 2   # skip ahead a week
    else:
        week += 1

        team_size = int(input("How many members? "))
for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name}")

    for value in range(0, 25, 5):
    print(value)