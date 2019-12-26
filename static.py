class Employee : 
    no_of_leaves = 8
    def __init__(self,name,id) :
      self.name = name
      self.id = id  
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves = leaves
    
    @classmethod
    def from_delimeter(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printsomething(a):
        
        print(f"you are good , {a}")



tarun = Employee.from_delimeter("tarun-101")
tarun.printsomething('tatrun')
Employee.printsomething("abcxyz")
print(tarun.id)