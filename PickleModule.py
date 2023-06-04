import pickle
example = {"FIRST": "1", "SECOUND": "2", "THREE": "3"}
Pickle_write = open("text.txt", "wb") #wb => write binary
pickle.dump(example, Pickle_write)
Pickle_write.close()
# pickle write
file = open("text.txt", "rb") #rb => read binary
dir = pickle.load(file)
print(dir)
# pickle read