import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    n = 3
    if len(opponent_history) < n:
        return random.choice(["R", "P", "S"])

    patterns = {}
    for i in range(len(opponent_history) - n):
        seq = "".join(opponent_history[i:i+n])       
        next_move = opponent_history[i+n]           
        if seq not in patterns:
            patterns[seq] = {"R": 0, "P": 0, "S": 0}
        patterns[seq][next_move] += 1

    last_seq = "".join(opponent_history[-n:])

    if last_seq in patterns:
        prediction = max(patterns[last_seq], key=patterns[last_seq].get)
    else:
        prediction = random.choice(["R", "P", "S"])

    beats = {"R": "P", "P": "S", "S": "R"}
    return beats[prediction]
