
from matplotlib import pyplot as plt


age_x=[25,26,27,28,29,30,31,32]
salary_y= [1200,2400,3400,2300,6000,9500,9900,10002]
plt.plot (age_x,salary_y,color='#553391',linestyle='--',linewidth= 3)

#salary_new= [2000,2800,4000,6000,10000,15000,17000,21000]
plt.bar(age_x,salary_y,color='#333333',linestyle='--',linewidth= 5)

plt.legend(['Gen case','Spec case'])
plt.xlabel("Ages")
plt.ylabel("Salary")
plt.title("Salary vs Age in Workers")

plt.grid(True)
plt.show()










