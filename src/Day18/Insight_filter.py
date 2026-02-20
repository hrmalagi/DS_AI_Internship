import sqlite3

# Connect to existing database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 1️⃣ FILTER: Data Science interns with stipend > 5000
print("Data Science Interns with stipend > 5000:")
cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")

for row in cursor.fetchall():
    print(row)

# 2️⃣ GROUP BY: Average stipend per track
print("\nAverage Stipend Per Track:")
cursor.execute("""
SELECT track, AVG(stipend)
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

# 3️⃣ COUNT: Number of interns per track
print("\nCount of Interns Per Track:")
cursor.execute("""
SELECT track, COUNT(*)
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

conn.close()