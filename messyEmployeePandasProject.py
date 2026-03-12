#messy data of emplyees
import pandas as pd
data = {
    "nm": ["  alice  ", "BOB", "Charlie", "alice  ", "EVE", "Frank"],
    "ag": [25, "abc", 22, 25, None, 30],
    "sal": [50000, 60000, None, 50000, 45000, None],
    "dept": ["HR", "it", "IT", None, "hr", "Finance"],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com", "alice@example.com", "eve@example.com", "frank@example.com"]
}
df = pd.DataFrame(data)
#rename columns
df = df.rename(columns={"nm": "name", "ag": "age", "sal": "salary", "dept": "department"})
#clean strings
df["name"] = df["name"].str.strip().str.title()
df["email"] = df["email"].str.lower()
df["department"] = df["department"].str.upper().fillna("UNKNOWN")
#fix age and missing salary
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(0)


#remove duplicates based on email
df = df.drop_duplicates(subset=["email"])
#ADD TAX COLUMN
df["tax"] = df["salary"] * 0.15
#print cleaned data
print("Cleaned Employee Data:")
print(df.head())
df.info()
print()
#export cleaned data
df.to_csv("cleaned_employees.csv", index=False)
df.to_excel("cleaned_employees.xlsx", index=False)