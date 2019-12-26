class Employee : 
    no_of_leaves = 8
    def __init__(self,name,id) :
      self.name = name
      self.id = id  
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves = leaves

class Programmer(Employee):
    def __init__(self,name,id,languages) :      #Constructor of child class             #super keyword can be used here
        self.name = name 
        self.id = id 
        self.languages=languages

    def printdata(self):
        print(f"The data of programmer is :{self.name},{self.id},{self.languages}")
        return 0 
prateek = Employee("Prateek",102)
tarun = Programmer("Tarun",101,["Python","Javascript"])
print(tarun.printdata())
