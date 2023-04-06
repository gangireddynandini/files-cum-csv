import csv
fil=input('enter file name:')
with open(fil,'r')as fp:
    obj=csv.reader(fp)
    for val in obj:
        for b in val:
            print(b)