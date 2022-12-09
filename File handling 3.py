fp=open("a.txt","w")
fp.write("Hello\n")
fp.write("Shilpa\n")
fp.write("Lecture of python")
fp.close()
with open("a.txt","r") as fp:
    data=fp.read()
    print(data)

# with open("a.txt","rb") as fp:
#     data=fp.read()
#     print(data)

with open("a.txt","r") as fp:
    data=fp.read(3)
    print(data)

with open("a.txt","r") as fp:
    data=fp.readline()
    print(data)


with open("a.txt","a") as fp:
    fp.writelines(["1","2","\n","1"])

with open("a.txt","r") as fp:
    data=fp.read()
    print(data)


