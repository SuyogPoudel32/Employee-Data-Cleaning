import numpy as np
import pandas as pd

df = pd.read_csv("Data_dub.csv")

df.replace([np.inf, -np.inf],np.nan,inplace=True)

mean_age = int(df["Age"].mean(skipna=True))

df[["Age","Experience(Year)"]] = df[["Age","Experience(Year)"]].fillna(mean_age)

df[["Age","Experience(Year)"]] = df[["Age","Experience(Year)"]].astype(int)



#Experience year sort the -ve value and other inappropriate Experience
mean_val = df["Experience(Year)"].mean()
df["Experience(Year)"] = np.where(
    (df["Experience(Year)"] < 0) | (df["Experience(Year)"] > 40),
    np.floor(mean_val * 10) / 10,   
    np.ceil(df["Experience(Year)"])
)

#Age extraordinary value fix
mask = df.query(
    "`Age` <0 or `Age` > 50 or `Age` <10"
).index
df.loc[mask,"Age"] = np.ceil(df["Age"].mean())


# Salary fix
salary_mean = df["Salary(INR)"].mean()
salary_std = df["Salary(INR)"].std()
Q1 = df["Salary(INR)"].quantile(0.25)
Q3 = df["Salary(INR)"].quantile(0.75)
IQR = Q3 - Q1

lower_salary = max(0, Q1 - 1.5*IQR)
upper_salary = Q3 + 1.5*IQR

df["Salary(INR)"] = np.where(
    (df["Salary(INR)"] < lower_salary) | (df["Salary(INR)"] > upper_salary),df["Salary(INR)"].median(),df["Salary(INR)"]
)
# df["Salary(INR)"].fillna(df["Salary(INR)"].median(),inplace=True) # throws error but works
df["Salary(INR)"] = df["Salary(INR)"].fillna(df["Salary(INR)"].median())
df.drop_duplicates(inplace=True)

print(df) #prints the data frame

#Cleaned data update
df.to_csv("Updated_Data.csv") # with index
df.to_csv("Updated_Data_withou_index.csv",index=False)  #without index