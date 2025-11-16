import random
from footbal import Player, Forward, Midfielder, Defender, Team, Match

def main():
    print("Hello from football-match!\n")

    # --- Create Players ---
    f1 = Forward("Messi", goals=10, assists=5, passes=20, shots=25, pace=90)
    f2 = Forward("Ronaldo", goals=8, assists=3, passes=15, shots=22, pace=85)

    m1 = Midfielder("Modric", goals=3, assists=10, passes=50, successful_passes=45, shots=5)
    m2 = Midfielder("Kante", goals=1, assists=6, passes=40, successful_passes=35, shots=3)

    d1 = Defender("Ramos", goals=2, assists=1, passes=30, shots=2, successful_tackles=20, total_tackles=25)
    d2 = Defender("Van Dijk", goals=1, assists=2, passes=35, shots=1, successful_tackles=22, total_tackles=25)

    # --- Create Teams ---
    team1 = Team("Team A")
    team1.add_player(f1)
    team1.add_player(m1)
    team1.add_player(d1)

    team2 = Team("Team B")
    team2.add_player(f2)
    team2.add_player(m2)
    team2.add_player(d2)

    # --- Simulate Match ---
    match = Match(team1, team2, duration=90, score="0:0")
    match.simulate_match()

    # --- Calculate Team Stats ---
    team1.calculate_team_stat()
    team2.calculate_team_stat()

    print(f"\n--- Team Stats ---")
    print(f"{team1.name} -> Total Goals: {team1.total_goals}, Total Shots: {team1.total_shots}")
    print(f"{team2.name} -> Total Goals: {team2.total_goals}, Total Shots: {team2.total_shots}")

    # --- Top Scorers ---
    top_scorer_team1 = max(team1.players, key=lambda p: p.goals)
    top_scorer_team2 = max(team2.players, key=lambda p: p.goals)

    print(f"\nTop Scorer of {team1.name}: {top_scorer_team1.name} ({top_scorer_team1.goals} goals)")
    print(f"Top Scorer of {team2.name}: {top_scorer_team2.name} ({top_scorer_team2.goals} goals)")

    # --- Optional: Possession Calculation ---
    def calculate_possession(team1: Team, team2: Team):
        total_shots = team1.total_shots + team2.total_shots
        if total_shots == 0:
            return (50, 50)
        t1_poss = (team1.total_shots / total_shots) * 100
        t2_poss = 100 - t1_poss
        return round(t1_poss, 1), round(t2_poss, 1)

    t1_poss, t2_poss = calculate_possession(team1, team2)
    print(f"\nPossession: {team1.name} {t1_poss}% - {team2.name} {t2_poss}%")

# --- Standard Python entry point ---
if __name__ == "__main__":
    main()
