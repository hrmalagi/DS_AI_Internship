raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_users=set(raw_logs)
print(unique_users)
print("ID05" in unique_users)
print("Rawlogs=",len(raw_logs))
print("Uniqueusers=",len(unique_users))