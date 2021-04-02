import os
# thinking
print("is i am learning")
list_of_files = os.listdir(path)

# txt files
num_txt = len([x for x in list_of_files if x.endswith(".txt")])
