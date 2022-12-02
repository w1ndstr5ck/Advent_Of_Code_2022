with open("E:\Code\Coding\Advent of Code 2022\Day_2_Input.txt", "r") as input:
    rounds = input.readlines()
    input.close()

score_lookup = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

score = 0
for round in rounds:
    score = score + score_lookup[round.strip("\n")]

print(score)

#find all unique rounds for the lookup table
def find_uniques(rounds):
    unique_rounds = []

    for round in rounds:
        if round not in unique_rounds:
            unique_rounds.append(round)

    for round in unique_rounds:
        print(round)

#find_uniques(rounds)
