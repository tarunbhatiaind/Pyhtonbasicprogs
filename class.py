class Employee : 
    no_of_leaves = 8
    def __init__(self,name,id) :
      self.name = name
      self.id = id  
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves = leaves
    # def printdetails(self):
    #     return f"Name is {self.name}.Id is {self.id}"


# tarun = Employee()
# rahul = Employee() 
# tarun.name = 'Tarun'
# tarun.id = 101
# rahul.name = 'Rahul'
# rahul.id = 102
# print(rahul.name)
# print(tarun.name)  
# print(rahul.no_of_leaves)
# Employee.no_of_leaves = 9
# print(rahul.no_of_leaves)
# print(tarun.printdetails())
# print(rahul.printdetails())

# cONSTRUCTOR IN PYTHON :


tarun = Employee("Tarun", 101)
rahul = Employee("Rahul", 102)
print(tarun.name)
print(rahul.id)
rahul.change_leaves(41)
print(tarun.no_of_leaves)