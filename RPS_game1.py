"""
import random
from RPS import player
import matplotlib.pyplot as plt

def play(player1, player2, num_games=1000):
    p1_prev, p2_prev = "", ""
    p1_score, p2_score = 0, 0
    for i in range(num_games):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if not valid_move(p1_move) or not valid_move(p2_move):
            print(f"Invalid move(s): {p1_move}, {p2_move}")
            break

        p1_prev, p2_prev = p1_move, p2_move

        if p1_move == p2_move:
            continue
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "P" and p2_move == "R") or \
             (p1_move == "S" and p2_move == "P"):
            p1_score += 1
        else:
            p2_score += 1

    print(f"{player1.__name__} vs {player2.__name__}")
    print(f"Player 1 wins: {p1_score}")
    print(f"Player 2 wins: {p2_score}")
    print(f"Win rate: {round(p1_score / (p1_score + p2_score) * 100, 2)}%")

def valid_move(move):
    return move in ["R", "P", "S"]

# --- تعريف البوتات الأربعة ---

def quincy(prev_play):
    # Quincy لديه سلسلة محددة مسبقاً
    choices = ["R", "P", "S", "R", "P"]
    return choices[(len(prev_play) % len(choices))]

def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        prev_play = random.choice(["R", "P", "S"])
    opponent_history.append(prev_play)
    guess = random.choice(["R", "P", "S"])
    if len(opponent_history) > 2:
        guess = opponent_history[-2]
    return {"R": "P", "P": "S", "S": "R"}[guess]

def kris(prev_play):
    if prev_play == "":
        return "R"
    if prev_play == "R":
        return "P"
    if prev_play == "P":
        return "S"
    return "R"

def mrugesh(prev_play, opponent_history=[]):
    # لا نضيف القيم الفارغة
    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # نحسب أكثر حركة تكررت في تاريخ الخصم
    most_common = max(set(opponent_history), key=opponent_history.count)

    # نرجع الحركة التي تغلب أكثر حركة متكررة
    return {"R": "P", "P": "S", "S": "R"}[most_common]

# اختبار ضد كل بوت
if __name__ == "__main__":
    print("Playing against Quincy:")
    play(player, quincy)

    print("\nPlaying against Abbey:")
    play(player, abbey)

    print("\nPlaying against Kris:")
    play(player, kris)

    print("\nPlaying against Mrugesh:")
    play(player, mrugesh)
    """