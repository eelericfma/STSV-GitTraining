import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
# for r, d, f in os.walk(thisdir):
#     for file in f:
#         #if file.endswith(".docx"):
#			# print complete file names 
#         	print(os.path.join(r, file)) 

ext_count = dict()
ext_count = {'No_Extension':0}
filenames = next(os.walk(thisdir))[2]
print(filenames)

for file in filenames:
	ext=file.split(".")[-1]
	#print(ext)
	if ext in ext_count:
		ext_count[ext]+= 1
		#print(ext+" found")
	elif ext==file:
		ext_count['No_Extension']+=1
		#print("no extension")	
	else:
		ext_count[ext]= 1
		#print(ext+" not found")

print (ext_count)
