# Employee Data Cleaning with Python (Pandas & NumPy)

This project demonstrates how to clean a messy employee dataset using Python, Pandas, and NumPy. The dataset contains 170+ employee records with intentional unrealistic, missing, and duplicate values for testing data cleaning techniques.

# Features

Replaces infinite (inf / -inf) values with NaN.

Fills missing Age and Experience(Year) values with the mean.

Converts Age and Experience(Year) columns to integers.

Handles unrealistic Age (negative, <10, or >50) by replacing with the mean age.

Handles unrealistic Experience(Year) (negative or >40) by replacing with the mean experience.

Cleans Salary(INR):

Replaces outliers (using IQR method) with the median salary.

Fills missing salaries with median.

Removes duplicate records to ensure data integrity.

Saves the cleaned dataset to CSV files:

Updated_Data.csv → with index

Updated_Data_without_index.csv → without index


# Purpose
This project is ideal for practicing data cleaning, handling outliers, NaN values, and duplicate records. It’s a practical example for data analysts, data scientists, or anyone learning Pandas and NumPy.
