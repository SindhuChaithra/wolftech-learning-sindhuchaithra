# importing pandas library
import pandas as pd
import pipeline as pd

# Create empty dataframe
df = pd.DataFrame()

# Creating a simple dataframe
df['name'] = ['Reema', 'Shyam', 'Jai',
              'Nimisha', 'Rohit', 'Riya']
df['gender'] = ['Female', 'Male', 'Male',
                'Female', 'Male', 'Female']
df['age'] = [31, 32, 19, 23, 28, 33]
# print(df)
# filtering by Gender and Annual Income
def filter_gender_income(dataframe, col1,col2):
    return data[(data[col1] == "Male") & (data[col2] >= 15) ]
# print(df)

# groupby mean and dropping ID columns
def mean_group(dataframe, col):
    return dataframe.groupby(col).mean().drop("age",axis=1)
# print(df)

# changing column names to uppercase
def uppercase_column_name(dataframe):
    dataframe.columns = dataframe.columns.str.upper()
    # print(df)
drop_age = pd.ColDrop('age')
df= drop_age(df)
print(df)
