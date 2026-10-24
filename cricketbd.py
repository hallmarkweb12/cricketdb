import sqlite3
import pandas as pd
conn = sqlite3.connect("cricket.db")
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_match;

CREATE TABLE IF NOT EXISTS Team(
   Team_id INTEGER PRIMARY KEY,
   Teamname TEXT
);
CREATE TABLE Match(
    match_id PRIMARY KEY,
    season_id INTEGER,
    match_winner INTEGER,
    win_margin INTEGER
);

CREATE TABLE Player_match(
  player_id INTEGER PRIMARY KEY,
  Match_id INTEGER
);

INSERT INTO Team VALUES
(1,"MCI"),(2,"AVL")
(3,"MUN"),(4,"Leeds")
(5,"Inter Miami");

INSERT INTO Match VALUES
(1,4,6,7),(23,45,23,1),(2,4,6,7),(4,5,1,5),(3,5,7,2),(4,9,3,6);

INSERT INTO Player_match VALUES
(3,101),(2,103),(4,100),(5,106),(7,109);
""")
conn.commit()
print("Database ready")
tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type ="Table";""",conn)
print(tables)

matches = pd.read_sql("""SELECT* FROM Match""",conn)
print(matches)