class Employee : 
    no_of_leaves = 8
    def __init__(self,name,id) :
      self.name = name
      self.id = id  
    @classmethod
    def from_str(cls,string):   
        #  params = string.split("-")
        #  return cls(params[0],params[1])
        return cls(*string.split("-"))

tarun = Employee.from_str("tarun-101")     
print(tarun.id)
