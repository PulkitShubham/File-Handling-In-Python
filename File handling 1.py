# File Handling
# File Name is the name of the file
# File Path is the location of the file
# Mode- It is the second argument in the open() function syntax. By default, it is set to read-only "r"
# In 'w'(write) mode, it overwrites the data present in the file
# In 'a'(append) mode, it appends the data to the file.Remember it does not overwrite rather append the data at the end
# of the pointer.
# Syntax:- f=open('sample1.txt','w') it will try to open a new file with write mode.
a1 = open("k22hw.txt","a")
a1.write("new\n")
a1.write("take care\n")
a1.write("overwrite\n")
a1.close()
a11=open("k22hw.txt","r")
print(a11.read())
a11.close()
