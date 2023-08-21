#Create salary.csv file which contain sid,sname,salary.
#Display the employee record whose name begins from "S‟ also show no. of employee with first letter "S‟ out of total
import csv
csv_rowlist=[['sid','sname','salary'],
             [1,'om',2000],
             [2,'sai',4500],
             [3,'ram',3000],
             [4,'shiv',2500],
             [5,'rudra',5000]],
with open('c:\\sqlite3\\csv\\salary.csv','w') as file:
    w= csv.writer(file)
    w.writerows(csv_rowlist)


    
    
      
