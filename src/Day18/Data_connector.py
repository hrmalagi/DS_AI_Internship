import sqlite3
import pandas as pd

# Connect to existing database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 1️⃣ Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# 2️⃣ Insert mentors (avoid duplicate inserts if already exists)
cursor.execute("DELETE FROM mentors")

cursor.execute("INSERT INTO mentors (mentor_name, track) VALUES ('Dr. Sharma', 'Data Science')")
cursor.execute("INSERT INTO mentors (mentor_name, track) VALUES ('Mr. Raj', 'Web Dev')")
cursor.execute("INSERT INTO mentors (mentor_name, track) VALUES ('Dr. Mehta', 'AI/ML')")

conn.commit()

# 3️⃣ INNER JOIN query
query = """
SELECT interns.name, interns.track, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# 4️⃣ Load result into Pandas DataFrame
df = pd.read_sql_query(query, conn)

print("Interns with their Mentors:")
print(df)

conn.close()