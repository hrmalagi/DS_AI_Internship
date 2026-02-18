import pandas as pd

# Step 1: Create dataset
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Blue"]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Step 2: Label Encoding for Transmission
df["Transmission"] = df["Transmission"].map({
    "Automatic": 0,
    "Manual": 1
})

# Step 3: One Hot Encoding for Color
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
print("\nEncoded Data:")
print(df)