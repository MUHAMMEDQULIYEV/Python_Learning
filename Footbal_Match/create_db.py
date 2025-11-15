import sqlite3
from footbal import Forward, Midfielder, Defender, Team, Match


DB_PATH = "football.db"


def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        total_goals INTEGER DEFAULT 0,
        total_shots INTEGER DEFAULT 0,
        possession REAL DEFAULT 0.0
    );
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT,
        goals INTEGER DEFAULT 0,
        assists INTEGER DEFAULT 0,
        passes INTEGER DEFAULT 0,
        shots INTEGER DEFAULT 0,
        pace INTEGER,
        successful_passes INTEGER,
        successful_tackles INTEGER,
        total_tackles INTEGER,
        team_id INTEGER,
        FOREIGN KEY(team_id) REFERENCES teams(id)
    );
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS matches (
        id INTEGER PRIMARY KEY,
        team1_id INTEGER,
        team2_id INTEGER,
        duration INTEGER,
        score TEXT,
        FOREIGN KEY(team1_id) REFERENCES teams(id),
        FOREIGN KEY(team2_id) REFERENCES teams(id)
    );
    """
    )

    conn.commit()


def insert_team(conn: sqlite3.Connection, team: Team) -> int:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO teams (name, total_goals, total_shots, possession) VALUES (?, ?, ?, ?)",
        (team.name, team.total_goals, team.total_shots, team.possession),
    )
    conn.commit()
    return cur.lastrowid


def insert_player(conn: sqlite3.Connection, player, team_id: int):
    cur = conn.cursor()
    cur.execute(
        """
    INSERT INTO players (
        name, position, goals, assists, passes, shots,
        pace, successful_passes, successful_tackles, total_tackles, team_id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            player.name,
            getattr(player, "position", None),
            getattr(player, "goals", 0),
            getattr(player, "assists", 0),
            getattr(player, "passes", 0),
            getattr(player, "shots", 0),
            getattr(player, "pace", None),
            getattr(player, "successful_passes", None),
            getattr(player, "successful_tackles", None),
            getattr(player, "total_tackles", None),
            team_id,
        ),
    )
    conn.commit()
    return cur.lastrowid


def insert_match(conn: sqlite3.Connection, match: Match, team1_id: int, team2_id: int):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO matches (team1_id, team2_id, duration, score) VALUES (?, ?, ?, ?)",
        (team1_id, team2_id, match.duration, match.score),
    )
    conn.commit()
    return cur.lastrowid


def build_db():
    # Recreate the same data from main.py
    f1 = Forward("Messi", goals=10, assists=5, passes=20, shots=25, pace=90)
    f2 = Forward("Ronaldo", goals=8, assists=3, passes=15, shots=22, pace=85)

    m1 = Midfielder(
        "Modric", goals=3, assists=10, passes=50, successful_passes=45, shots=5
    )
    m2 = Midfielder(
        "Kante", goals=1, assists=6, passes=40, successful_passes=35, shots=3
    )

    d1 = Defender(
        "Ramos",
        goals=2,
        assists=1,
        passes=30,
        shots=2,
        successful_tackles=20,
        total_tackles=25,
    )
    d2 = Defender(
        "Van Dijk",
        goals=1,
        assists=2,
        passes=35,
        shots=1,
        successful_tackles=22,
        total_tackles=25,
    )

    # Note: the local Team signature in the project expects several parameters.
    # Provide default values and compute stats manually below.
    team1 = Team("Team A", [], 0, 0, 0.0)
    team1.add_player(f1)
    team1.add_player(m1)
    team1.add_player(d1)

    team2 = Team("Team B", [], 0, 0, 0.0)
    team2.add_player(f2)
    team2.add_player(m2)
    team2.add_player(d2)

    # Simulate match (the Match.simulate_match signature in the repo expects args)
    match = Match(team1, team2, duration=90, score="0:0")
    try:
        match.simulate_match(team1, team2, match.score, match.duration)
    except TypeError:
        # Fallback if signature accepts no args
        match.simulate_match()

    # Calculate team stats manually (some repo versions change Team.calculate_team_stat signature)
    team1.total_goals = sum(p.goals for p in team1.players)
    team1.total_shots = sum(p.shots for p in team1.players)
    team2.total_goals = sum(p.goals for p in team2.players)
    team2.total_shots = sum(p.shots for p in team2.players)

    # Optionally calculate possession by shots (same logic as main)
    total_shots = team1.total_shots + team2.total_shots
    if total_shots == 0:
        team1.possession, team2.possession = 50.0, 50.0
    else:
        t1_poss = (team1.total_shots / total_shots) * 100
        team1.possession = round(t1_poss, 1)
        team2.possession = round(100 - t1_poss, 1)

    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)

    t1_id = insert_team(conn, team1)
    t2_id = insert_team(conn, team2)

    # Insert players
    for p in team1.players:
        insert_player(conn, p, t1_id)
    for p in team2.players:
        insert_player(conn, p, t2_id)

    # Insert match
    insert_match(conn, match, t1_id, t2_id)

    # Print a short summary
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM teams")
    teams_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM players")
    players_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM matches")
    matches_count = cur.fetchone()[0]

    print(
        f"Database '{DB_PATH}' created:\n  teams={teams_count}, players={players_count}, matches={matches_count}"
    )
    conn.close()


if __name__ == "__main__":
    build_db()
