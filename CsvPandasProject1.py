import pandas as pd
# create student data as a dictionary
data = {
    "name":["Minhaz","Mousumi","Luis","Rahman","Murshida", "Mouli","Rajon", "Rafi"],
    "age":[23, 21, 23, 23, 21, 20, 24, 22],
    "grade":["A", "B", "C", "C", "D", "A", "B", "C"],
    "score":[90,65,57, 58, 52, 86, 67, 58],
    "city":["Sylhet", "Chittagong", "Sylhet", "Rajshahi", "Sylhet", "Barisal", "Mymensingh", "Rangpur"]
}
# convert to dataframe and save as csv
df = pd.DataFrame(data)
df.to_csv("studentsPandaProject.csv", index=False)
print("CSV created!")
# read the csv back into a dataframe
df = pd.read_csv("studentsPandaProject.csv")
#print shape
print(df.shape)
#info and describe
df.info()
print(df.describe())
print()
#filter students with score above 75
high_scorers = df[df["score"] > 75]
print("Students with score above 75:")
print(high_scorers)
#export high scores to excel
high_scorers.to_excel("high_scorers.xlsx", index=False)
print("\nHigh scorers exported to Excel!")
#filter students from Sylhet
sylhet_students = df[df["city"] == "Sylhet"]
print("\nStudents from Sylhet:")
print(sylhet_students)
#export Sylhet students to excel
sylhet_students.to_excel("sylhet_students.xlsx", index=False)
print("\nSylhet students exported to Excel!")