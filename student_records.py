import pandas as pd

data = pd.read_csv("marks.csv")

print("Student Records:")
print(data)

print("\nAverage Score:")
print(data["Score"].mean())

print("\nHighest Score:")
print(data["Score"].max())