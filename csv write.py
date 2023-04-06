import csv
filename=input('enter filename:')
with open(filename,'w')as fp:
    colnames=['name','branch','year','cgpa']
    rows=[['1','nandu','eee','4','50%'],
          ['2','divya','cse','3','40%'],
          ['3','joshna','mech','2','60%'],
          ['4','sree','ece','4','40%'],
          ['5','swetha','aeronautical','3','78%']]
    obj=csv.writer(fp)
    obj.writerow(colnames)
    obj.writerows(rows)