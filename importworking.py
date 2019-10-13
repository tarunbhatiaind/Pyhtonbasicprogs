# to get data from different class or packages
# from sklearn.ensemble import RandomForestClassifier
# print(RandomForestClassifier())

# you can create many functions in a file and use them in your code
import fileimport # better way to import rathter then to import var/class/functions or anything
print(fileimport.a)
# made fileimport and made a variable a in it with init value
from fileimport  import a
print(a)
fileimport.anyfunction("my string printed !") # anyfunction() made inside the file fileimport and called from here !