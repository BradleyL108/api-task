import csv
with open('afl_stats.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Rainfall(mm)'], row['Year'])




print(row)

"""import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('afl_stats.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row['Rainfall(mm)']))
        y.append(int(row['Year']))


plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: People and Expenses')

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.show()
"""
