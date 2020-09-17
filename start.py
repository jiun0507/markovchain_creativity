# 요가 자세 -> 다양한 콤피네이션을 창조

import random

# The statespace
states = ["big-toe","boat","bow", "chair", "corpse", "cow", "crow", "dolphin", "downward-facing-dog", "eight-angle", "legs-up-the-wall", "net-bearer-bond", "revolved-side-angle"]

# Possible sequences of events
transitionCombinations = [
    [
        cur_pose + ":" + next_pose for next_pose in states
    ] for cur_pose in states
]


# Probabilities matrix (transition matrix)
transitionMatrix = [
    [random.randrange(1, 50) for i in range(len(transitionCombinations))] for i in range(len(transitionCombinations))
]
for row in transitionMatrix:
    sum_row = sum(row)
    for i in range(0, len(row)):
        row[i]= row[i]/sum_row

def get_sequence_of_yoga_moves(length: int):
    cur = random.randint(0, 12)
    print("The first move is: ", states[cur])
    sequence = [states[cur]]
    length -= 1
    while length>0:
        chance = random.uniform(0, 1)
        cumulative = 0
        index = 0
        for elem in transitionMatrix[cur]:
            cumulative += elem
            if cumulative > chance:
                cur = index
                sequence.append(states[index])
                break
            index += 1
        length -= 1
    return sequence

print(get_sequence_of_yoga_moves(10))

