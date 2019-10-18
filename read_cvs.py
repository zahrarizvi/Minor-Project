import csv
new_table = []
def read_cvs():
    with open ('Task_Training_Data .csv','r') as csvfile:
        content = csv.reader(csvfile)
        for row in content:
            new_table.append(row[:2])
        return new_table
read_cvs()