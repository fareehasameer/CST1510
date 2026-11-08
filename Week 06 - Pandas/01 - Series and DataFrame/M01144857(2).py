
import pandas as pd

name = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
math = [85, 90, 72, 60, 95]
science = [78, 88, 85, 55, 92]

students=pd.DataFrame({"name": name, "math": math, "science": science})
students["average"]=(students["math"]+students["science"])/2
print(students)
print()

print(students[["name", "average"]]) #subset of the dataframe
print()

print(students[students["average"]>=80]) #80+ marks
print()

print(students[(students["math"]>=90)&(students["science"]>=90)]) #90+in math AND 90+ in science