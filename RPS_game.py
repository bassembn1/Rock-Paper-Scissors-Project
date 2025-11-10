
"""
 
import random
import matplotlib.pyplot as plt
from RPS import player


def valid_move(move):
    return move in ["R", "P", "S"]


def play(player1, player2, num_games=200):
    p1_prev, p2_prev = "", ""
    p1_score, p2_score = 0, 0

    p1_scores = []
    p2_scores = []
    rounds = []

    p1_moves = {"R": 0, "P": 0, "S": 0}
    p2_moves = {"R": 0, "P": 0, "S": 0}

    for i in range(1, num_games + 1):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if not valid_move(p1_move) or not valid_move(p2_move):
            print(f"Invalid move(s): {p1_move}, {p2_move}")
            break

        p1_prev, p2_prev = p1_move, p2_move

        p1_moves[p1_move] += 1
        p2_moves[p2_move] += 1

        if p1_move == p2_move:
            pass
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "P" and p2_move == "R") or \
             (p1_move == "S" and p2_move == "P"):
            p1_score += 1
        else:
            p2_score += 1

        p1_scores.append(p1_score)
        p2_scores.append(p2_score)
        rounds.append(i)

    print(f"{player1.__name__} vs {player2.__name__}")
    print(f"Player 1 wins: {p1_score}")
    print(f"Player 2 wins: {p2_score}")
    total = p1_score + p2_score
    if total > 0:
        print(f"Win rate: {round(p1_score / total * 100, 2)}%")

    show_graphs(player1.__name__, player2.__name__, rounds, p1_scores, p2_scores, p1_moves, p2_moves)


def show_graphs(p1_name, p2_name, rounds, p1_scores, p2_scores, p1_moves, p2_moves):
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(rounds, p1_scores, label=f"{p1_name} score", linewidth=2)
    plt.plot(rounds, p2_scores, label=f"{p2_name} score", linewidth=2)
    plt.title("Score Evolution")
    plt.xlabel("Round")
    plt.ylabel("Score")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.bar(p1_moves.keys(), p1_moves.values(), color='blue')
    plt.title(f"{p1_name} move distribution")
    plt.xlabel("Move")
    plt.ylabel("Count")

    plt.subplot(2, 2, 3)
    plt.bar(p2_moves.keys(), p2_moves.values(), color='orange')
    plt.title(f"{p2_name} move distribution")
    plt.xlabel("Move")
    plt.ylabel("Count")

    plt.subplot(2, 2, 4)
    plt.bar([p1_name, p2_name], [p1_scores[-1], p2_scores[-1]], color=['green', 'red'])
    plt.title("Final Score Comparison")

    plt.tight_layout()
    plt.show()

def quincy(prev_play):
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(prev_play) % len(choices)] if prev_play else random.choice(choices)


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
    if prev_play:
        opponent_history.append(prev_play)
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    most_common = max(set(opponent_history), key=opponent_history.count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


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
    
import random
import matplotlib.pyplot as plt
import pandas as pd
from RPS import player


def valid_move(move):
    return move in ["R", "P", "S"]


def play(player1, player2, num_games=1000):
    p1_prev, p2_prev = "", ""
    p1_score, p2_score = 0, 0

    rounds = []
    p1_scores = []
    p2_scores = []
    results = [] 

    p1_moves = {"R": 0, "P": 0, "S": 0}
    p2_moves = {"R": 0, "P": 0, "S": 0}

    for i in range(1, num_games + 1):
        p1_move = player1(p2_prev)
        p2_move = player2(p1_prev)

        if not valid_move(p1_move) or not valid_move(p2_move):
            print(f"Invalid move(s): {p1_move}, {p2_move}")
            break

        p1_prev, p2_prev = p1_move, p2_move

        p1_moves[p1_move] += 1
        p2_moves[p2_move] += 1

        winner = None
        if p1_move == p2_move:
            winner = "Draw"
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "P" and p2_move == "R") or \
             (p1_move == "S" and p2_move == "P"):
            p1_score += 1
            winner = "Player 1"
        else:
            p2_score += 1
            winner = "Player 2"

        rounds.append(i)
        p1_scores.append(p1_score)
        p2_scores.append(p2_score)

        results.append({
            "Round": i,
            "Player1_Move": p1_move,
            "Player2_Move": p2_move,
            "Winner": winner,
            "P1_Total_Score": p1_score,
            "P2_Total_Score": p2_score
        })

    df = pd.DataFrame(results)
    print("\n📊 Sample of Results:")
    print(df.head(10)) 

    match_name = f"{player1.__name__}_vs_{player2.__name__}.csv"
    df.to_csv(match_name, index=False)
    print(f"\n✅ Results saved to: {match_name}")

    total = p1_score + p2_score
    win_rate = round(p1_score / total * 100, 2) if total > 0 else 0
    print(f"\n🏆 Final Results — {player1.__name__} vs {player2.__name__}")
    print(f"Player 1 Wins: {p1_score} | Player 2 Wins: {p2_score} | Win Rate: {win_rate}%")

    show_graphs(player1.__name__, player2.__name__, rounds, p1_scores, p2_scores, p1_moves, p2_moves)

    return {
        "Opponent": player2.__name__,
        "P1_Wins": p1_score,
        "P2_Wins": p2_score,
        "Win_Rate": win_rate
    }


def show_graphs(p1_name, p2_name, rounds, p1_scores, p2_scores, p1_moves, p2_moves):
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 2, 1)
    plt.plot(rounds, p1_scores, label=f"{p1_name}", linewidth=2)
    plt.plot(rounds, p2_scores, label=f"{p2_name}", linewidth=2)
    plt.title("Score Evolution")
    plt.xlabel("Round")
    plt.ylabel("Score")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.bar(p1_moves.keys(), p1_moves.values(), color='blue')
    plt.title(f"{p1_name} move distribution")

    plt.subplot(2, 2, 3)
    plt.bar(p2_moves.keys(), p2_moves.values(), color='orange')
    plt.title(f"{p2_name} move distribution")

    plt.subplot(2, 2, 4)
    plt.bar([p1_name, p2_name], [p1_scores[-1], p2_scores[-1]], color=['green', 'red'])
    plt.title("Final Score Comparison")

    plt.tight_layout()
    plt.show()


def quincy(prev_play):
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(prev_play) % len(choices)] 
# if prev_play else random.choice(choices)


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
    if prev_play:
        opponent_history.append(prev_play)
    if not opponent_history:
        return random.choice(["R", "P", "S"])
    most_common = max(set(opponent_history), key=opponent_history.count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


if __name__ == "__main__":
    results_summary = []

    for bot in [quincy, abbey, kris, mrugesh]:
        print(f"\n🎮 Playing against {bot.__name__}...")
        result = play(player, bot)
        results_summary.append(result)

    summary_df = pd.DataFrame(results_summary)
    print("\n📈 Summary of all matches:")
    print(summary_df)

    summary_df.to_csv("all_results_summary.csv", index=False)
    print("\n✅ Saved global summary to: all_results_summary.csv")
