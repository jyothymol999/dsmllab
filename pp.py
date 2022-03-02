import csv
with open('D:\DSML lab\iris.data','rb') as csvfile:
    lines=csv.read(csvfile)
    for row in lines:
        print','.join(row)