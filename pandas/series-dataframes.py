import pandas as pd
# sd=pd.Series()
# print(sd)
# # creating empty series
# # passing aruguments using list
l=[10,20,30,40]
sd=pd.Series(l)
# print(sd)
# # using index value
# sd=pd.Series(l, index=['a','b','c','d'])
# print(sd)
# # to work with array we need numpy
import numpy as np
a=np.array([1,2,3,4])
# print(a)
a=np.array([1,2,3,4]) # list with series
s=pd.Series(a)
# # print(a)
# # dict with series
d=('a:10', 'b:20' , 'c:30')
s=pd.Series(d)
# print(d)
#
#
# # dataframes using pandas
d=pd.read_csv("C:\\Users\\Sindhu\\data.csv")
print(d)
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# # print(df)
# #use a list of indexes:
# # print(df.loc[[0, 1]])
# # Add a list of names to give each row a name:
# data = {"calories": [420, 380, 390],
#             "duration": [50, 40, 45]}
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# # print(df)
# # Get a quick overview by printing the first 10 rows of the DataFrame:
# df = pd.read_csv('C:\\Users\\Sindhu\\data.csv')
#
# # print(df.head(10))
# # There is also a tail()  and head() method for viewing the last rows of the DataFrame.
# # print(df.tail())
# # Remove all rows with NULL values::
#
#
# df = pd.read_csv('C:\\Users\\Sindhu\\data.csv')
#
# df.dropna(inplace = True)
#
# # print(df.to_string())
# x = df["Calories"].mean()
# # print(x)
# # Calculate the MEAN,
# x = df["Calories"].median()
# #  (the sum of all values divided by number of values).
# # Calculate the MEAN,and replace any empty values with it:
# df["Calories"].fillna(x, inplace = True)
# # print(x)
# # Returns True for every row that is a duplicate, othwerwise False:
# # print(df.duplicated())
# # there is no duplicate values present