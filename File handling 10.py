import pickle
class Student:
    def __init__(self,name,roll,section):
        self.name=name
        self.roll=roll
        self.section=section

    def display(self):
        print(self.name, self.roll, self.section )
with open("a100.txt",'wb') as f:
    st1=Student('A',12,'xxx') # Object created with arg will call init method
    pickle.dump(st1,f)
    print('Pickling done')

with open('a100.txt','rb') as f:
    obj=pickle.load(f)
    print('unpickling done')
    obj.display()


