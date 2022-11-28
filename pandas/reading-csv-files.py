import pandas as pd
# df= pd.read_csv("C:\\Users\\Sindhu\\new.data.csv")
# print(df)
# df = pd.read_csv("C:\\Users\\Sindhu\\new.data.csv", skiprows=1)
# print(df) # to skip any rows from the dataset
# df = pd.read_csv("C:\\Users\\Sindhu\\new.data.csv",header=None)
# print(df)
# to find out the header, in the given dataset as header= None
# df = pd.read_csv("C:\\Users\\Sindhu\\new.data.csv",header=None, names=["Duration","Pulse","Maxpulse","Calories"])
# print(df)
# we can use name argument in read csv file into colum names sequences
# df.to_csv('new.csv')
# print(df)
# df = pd.read_csv("C:\\Users\\Sindhu\\data.csv", na_values = ["not avaliable", "n.a"])
# print(df)
# it reads not a number values in your data we use n.a
# df.to_csv('new.csv', index =False)
# print(df)
# if there are index present in the data to remove we use index function
# df.to_csv("C:\\Users\\Sindhu\\data.csv",columns=['Pulse', 'Calories'])
# print(df)