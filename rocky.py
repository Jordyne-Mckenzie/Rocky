history = [
     {
        "round": 1,
       "player": "rock",
         "opponent": "paper",
         "round_winner": "Opp"
     },
     {
         "round": 2,
         "player": "scissors",
         "opponent": "paper",
         "round_winner": "Player"
     }
 ]
import random
def rocky(round_history):
    if not history:
       return(random.choice(["rock", "paper", "scissors"]))
    opponent_move = [past_history["opponent"] for past_history in round_history]
    counts = {"rock":opponent_move.count("rock"),"paper":opponent_move.count("paper"),"scissors":opponent_move.count("scissors")}
    used_most_move = max(counts, key=counts.get)
    counter = {"paper":"scissors","rock":"paper","scissors":"rock"}
    return counter[used_most_move]
print(rocky(history))