# Dictionaries
phonebook = {
    "abc" : 940123890,
    "Jack" : 9848757868,
    "any" : 947662781
}
print(phonebook)
# Iterating over dictionaries
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))