#creation of a bar-plot
from matplotlib import pyplot as plt
students={"Anand":87,"Mat":82,"Jack":97}
names=list(students.keys())#for creating the x-axis 
values=list(students.values())#for creating the y-axis
plt.barh(names,values,color='r')#to create horizontal use plt.barh
#to create vertical use plt.bar
#attaributes
plt.title("perfromance")
plt.xlabel("name of the students")
plt.ylabel("marks obtained")
print(plt.show())