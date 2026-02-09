name=input("Enter your name:")
goal=input("Enter your daily goal:")
with open("journal.txt","a") as file:
    file.write(f"Name:{name}, DailyGoal:{goal}")

print("Journal has been updated")