# Dump for writing function and load for reading function
import pickle
animalDict={'cat':2,'Dog':7,'Lion':4,'Tiger':9,'Leopard':11}
outfile=open('animals.txt','wb')
pickle.dump(animalDict,outfile)
outfile.close()
fst=open("animals.txt",'rb')
data=pickle.load(fst)
print(data)