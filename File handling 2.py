# a=open("Task.txt","a")
# print(a.read()) # When file is opened in a and w mode,one cannot read the contents

# Create a file with name myfile.txt and write something
file1=open("myfile.txt","w")
file1.write("new\n")
file1.write("take care\n")
file1.write("overwrite\n")
file1.close()
file1=open("myfile.txt","r")

print("Output of Read function is ")
print(file1.read(5))
file1.seek(0) # To go into the position again here it is moving to the beginning
# To show difference between read and readline
print("Output of Read(9) function is")
print(file1.read(9))
print()
file1.seek(0)
print("Output of Readline(9) function is")
print(file1.readline(9))
file1.seek(0)
print("Output of Readlines function is")
print(file1.readlines())
print()
file1.close()

