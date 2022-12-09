# File handling using read and write both
f1=open("demo.txt","w+")  # w+ means write and read both
n="Hello this is python"
f1.write(n)
f1.seek(0)
print(f1.read(6))
f1.close()
f11=open("demo.txt","r")
print(f11.read())
f11.close()
# Seek:-takes the pointer to that argument
f12=open("demo.txt","a")
# f12.seek(5) # Used for random access
print(f12.tell())  # tell shows the current position of the pointer
f12.close()
# Things learnt:
# How to create a file?
# Different modes(12) but focus is on 3
# How to write contents in a file
# How to read contents of a file using read,readline, readlines
