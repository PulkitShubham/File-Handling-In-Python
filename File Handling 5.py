# Python program to illustrate
# Append vs write mode
file1=open("myfile1.txt","w") # connect
L=["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L) # Writing the list in file where list is object
file1.close() # Disconnect

# Append adds at last
file1=open("myfile1.txt","a") # append mode
file1.write("Today \n")
file1.close()


file1=open("myfile1.txt","rb") # here b stands for binary format
print("Output of Readlines after appending")
print(file1.readline().decode('utf-8')) # decoding mechanism for this function
# print(file1.readlines())
print()
