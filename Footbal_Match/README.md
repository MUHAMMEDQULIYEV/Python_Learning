(Quick helper) Create an SQLite database from the sample data in the project

Run the script to create `football.db` in the project root:

```bash
python3 create_db.py
```

This will create an SQLite database `football.db` with three tables:
- `teams` (id, name, total_goals, total_shots, possession)
- `players` (id, name, position, goals, assists, passes, shots, pace, successful_passes, successful_tackles, total_tackles, team_id)
- `matches` (id, team1_id, team2_id, duration, score)

Quick inspect with Python:

```python
import sqlite3
conn = sqlite3.connect('football.db')
cur = conn.cursor()
cur.execute("SELECT name FROM teams;")
print(cur.fetchall())
conn.close()
```

If you'd like, I can also add helper queries or a small CLI to inspect the database.

