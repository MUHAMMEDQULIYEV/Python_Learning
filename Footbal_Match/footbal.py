import random


class Player:
    def __init__(
        self,
        name: str,
        position: str,
        goals: int,
        assists: int,
        passes: int,
        shots: int,
    ):
        self.name = name
        self.position = position
        self.goals = goals
        self.assists = assists
        self.passes = passes
        self.shots = shots

    def update_stats(self, goals=0, assists=0, passes=0, shots=0):
        self.goals += goals
        self.assists += assists
        self.passes += passes
        self.shots += shots


class Forward(Player):
    def __init__(self, name, goals=0, assists=0, passes=0, shots=0, pace=0):
        super().__init__(name, "Forward", goals, assists, passes, shots)
        self.pace = pace

    def finishing(self):
        return self.goals / self.shots if self.shots > 0 else 0


class Midfielder(Player):
    def __init__(
        self, name, goals=0, assists=0, passes=0, successful_passes=0, shots=0
    ):
        super().__init__(name, "Midfielder", goals, assists, passes, shots)
        self.successful_passes = successful_passes

    def pass_accuracy(self):
        return self.successful_passes / self.passes if self.passes > 0 else 0


class Defender(Player):
    def __init__(
        self,
        name,
        goals=0,
        assists=0,
        passes=0,
        shots=0,
        successful_tackles=0,
        total_tackles=0,
    ):
        super().__init__(name, "Defender", goals, assists, passes, shots)
        self.successful_tackles = successful_tackles
        self.total_tackles = total_tackles

    def tackle_success(self):
        return (
            self.successful_tackles / self.total_tackles
            if self.total_tackles > 0
            else 0
        )


class Team:
    def __init__(self, name: str, players: list[Player] = None):
        self.name = name
        self.players = players if players is not None else []
        self.total_goals = 0
        self.total_shots = 0
        self.possession = 0.0

    def add_player(self, player: Player):
        self.players.append(player)

    def calculate_team_stat(self):
        self.total_goals = sum(player.goals for player in self.players)
        self.total_shots = sum(player.shots for player in self.players)

"""  class Team:
    def __init__(self, name: str, players: list[Player] = None):
        self.name = name
        self.players = players if players is not None else []
        self.total_goals = 0
        self.total_shots = 0
        self.possession = 0.0

    def add_player(self, player: Player):
        self.players.append(player)

    def calculate_team_stat(self):
        self.total_goals = sum(player.goals for player in self.players)
        self.total_shots = sum(player.shots for player in self.players)
"""





class Match:
    def __init__(self, team1, team2, duration, score):
        self.team1 = team1
        self.team2 = team2
        self.duration = duration
        self.score = "0:0"

    def simulate_match(self):
        goals_team1 = random.randint(0, 5)
        goals_team2 = random.randint(0, 5)
        self.score = f"{goals_team1}:{goals_team2}"
        print(f"Match Result: {self.team1.name} {self.score} {self.team2.name}")

