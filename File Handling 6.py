fin=open('myfile1.txt','r')
fout=open('outputData3.txt','w')
for var in fin:
    fout.write(var)
fin.close()
fout.close()
fin=open('outputData3.txt','r')
for line in fin:
    print(line,end='')
fin.close()


