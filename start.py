# 요가 자세 -> 다양한 콤피네이션을 창조

import numpy
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


# # A function that implements the Markov model to forecast the state/mood.
# def activity_forecast(days):
#     # Choose the starting state
#     activityToday = "Sleep"
#     print("Start state: " + activityToday)
#     # Shall store the sequence of states taken. So, this only has the starting state for now.
#     activityList = [activityToday]
#     i = 0
#     # To calculate the probability of the activityList
#     prob = 1
#     while i != days:
#         if activityToday == "Sleep":
#             change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
#             if change == "SS":
#                 prob = prob * 0.2
#                 activityList.append("Sleep")
#                 pass
#             elif change == "SR":
#                 prob = prob * 0.6
#                 activityToday = "Run"
#                 activityList.append("Run")
#             else:
#                 prob = prob * 0.2
#                 activityToday = "Icecream"
#                 activityList.append("Icecream")
#         elif activityToday == "Run":
#             change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
#             if change == "RR":
#                 prob = prob * 0.5
#                 activityList.append("Run")
#                 pass
#             elif change == "RS":
#                 prob = prob * 0.2
#                 activityToday = "Sleep"
#                 activityList.append("Sleep")
#             else:
#                 prob = prob * 0.3
#                 activityToday = "Icecream"
#                 activityList.append("Icecream")
#         elif activityToday == "Icecream":
#             change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
#             if change == "II":
#                 prob = prob * 0.1
#                 activityList.append("Icecream")
#                 pass
#             elif change == "IS":
#                 prob = prob * 0.2
#                 activityToday = "Sleep"
#                 activityList.append("Sleep")
#             else:
#                 prob = prob * 0.7
#                 activityToday = "Run"
#                 activityList.append("Run")
#         i += 1
#     print("Possible states: " + str(activityList))
#     print("End state after "+ str(days) + " days: " + activityToday)
#     print("Probability of the possible sequence of states: " + str(prob))

# # Function that forecasts the possible state for the next 2 days
# activity_forecast(2)