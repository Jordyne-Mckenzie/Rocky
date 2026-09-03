# history = [
#     {
#         "round": 1,
#         "player": "Rock",
#         "opponent": "Paper",
#         "round_winner": "Opp"
#     },
#     {
#         "round": 2,
#         "player": "Scissors",
#         "opponent": "Paper",
#         "round_winner": "Player"
#     }
# ]
import random
def rocky():
    return(random.choice(["rock", "paper", "scissors"]))


print(rocky())
