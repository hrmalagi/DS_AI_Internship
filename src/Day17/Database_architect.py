import sqlite3

# Step 1: Create database (file will be created automatically)
conn = sqlite3.connect("internship.db")

# Step 2: Create cursor
cursor = conn.cursor()

# Step 3: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Step 4: Insert 5 rows
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Harsha', 'Data Science', 10000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Aman', 'Web Dev', 8000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Sneha', 'Data Science', 12000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Ravi', 'AI/ML', 15000)")
cursor.execute("INSERT INTO interns (name, track, stipend) VALUES ('Priya', 'Web Dev', 9000)")

# Save changes
conn.commit()

# Step 5: Query only name and track
cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

# Close connection
conn.close()