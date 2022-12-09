f1=open("myfile1.txt","r")
# for var in f1:
#     l1=var.split(" ")
#     print(len(l1))
charCount=wordCount=lineCount=0
for line in f1:
    lineCount+=1
    wordCount+=len(line.split())
    charCount+=len(line)
print("line count =",lineCount)
print("Word count =",wordCount)
print("Char count =",charCount)
