import pandas as px

# create dataframe
df = px.DataFrame({
    'Course': ['BBA', 'BCA', 'BBA', 'BCA', 'BCA'],
    'Student Name': ['Rishabh', 'Rahul', 'Suraj', 'Mukul', 'Vinit'],
    'Age': [21, 22, 23, 22, 23]})

# print original dataframe
print("original dataframe")
#print(df)

# counts Groupby value
df = df.groupby(['Course', 'Student Name', 'Age']).size().unstack(fill_value=0)

# print dataframe
print("Result :")
#print(df)


# def myFun(*argv):  #to create a function  we use def // by using * we can pass mulpile argumets at time it can store aruguments in function
#     for arg in argv: #for this im using for loop to print the function
#         print(arg)
#
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

