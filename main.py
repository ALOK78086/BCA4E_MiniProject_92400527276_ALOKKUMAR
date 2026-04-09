import sqlite3
from pathlib import Path


DEFAULT_STATS = {
    "high_score": 0,
    "matches_played": 0,
    "wins": 0,
    "total_kills": 0,
    "total_damage_dealt": 0.0,
    "total_damage_taken": 0.0,
    "best_level": 1,
    "best_survival_seconds": 0.0,
}


def _connect(db_path):
    connection = sqlite3.connect(Path(db_path))
    connection.row_factory = sqlite3.Row
    return connection


def init_database(db_path):
    with _connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS player_stats (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                high_score INTEGER NOT NULL DEFAULT 0,
                matches_played INTEGER NOT NULL DEFAULT 0,
                wins INTEGER NOT NULL DEFAULT 0,
                total_kills INTEGER NOT NULL DEFAULT 0,
                total_damage_dealt REAL NOT NULL DEFAULT 0,
                total_damage_taken REAL NOT NULL DEFAULT 0,
                best_level INTEGER NOT NULL DEFAULT 1,
                best_survival_seconds REAL NOT NULL DEFAULT 0,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS match_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                won INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                survival_seconds REAL NOT NULL,
                damage_dealt REAL NOT NULL,
                damage_taken REAL NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.execute(
            """
            INSERT OR IGNORE INTO player_stats (id)
            VALUES (1)
            """
        )
        connection.commit()


def load_game_data(db_path, recent_limit=5):
    with _connect(db_path) as connection:
        stats_row = connection.execute(
            """
            SELECT
                high_score,
                matches_played,
                wins,
                total_kills,
                total_damage_dealt,
                total_damage_taken,
                best_level,
                best_survival_seconds
            FROM player_stats
            WHERE id = 1
            """
        ).fetchone()
        stats = dict(DEFAULT_STATS)
        if stats_row:
            stats.update(dict(stats_row))

        recent_matches = [
            dict(row)
            for row in connection.execute(
                """
                SELECT score, won, level_reached, survival_seconds, created_at
                FROM match_history
                ORDER BY id DESC
                LIMIT ?
                """,
                (recent_limit,),
            ).fetchall()
        ]

    return stats, recent_matches


def record_match(
    db_path,
    *,
    score,
    won,
    level_reached,
    survival_seconds,
    damage_dealt,
    damage_taken,
):
    with _connect(db_path) as connection:
        connection.execute(
            """
            INSERT INTO match_history (
                score,
                won,
                level_reached,
                survival_seconds,
                damage_dealt,
                damage_taken
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                int(score),
                1 if won else 0,
                int(level_reached),
                float(survival_seconds),
                float(damage_dealt),
                float(damage_taken),
            ),
        )
        connection.execute(
            """
            UPDATE player_stats
            SET
                high_score = MAX(high_score, ?),
                matches_played = matches_played + 1,
                wins = wins + ?,
                total_kills = total_kills + ?,
                total_damage_dealt = total_damage_dealt + ?,
                total_damage_taken = total_damage_taken + ?,
                best_level = MAX(best_level, ?),
                best_survival_seconds = MAX(best_survival_seconds, ?),
                updated_at = CURRENT_TIMESTAMP
            WHERE id = 1
            """,
            (
                int(score),
                1 if won else 0,
                int(score),
                float(damage_dealt),
                float(damage_taken),
                int(level_reached),
                float(survival_seconds),
            ),
        )
        connection.commit()
