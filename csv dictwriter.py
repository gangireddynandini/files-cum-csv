import csv

filename=input('enter filename:')
with open(filename,'w')as fp:
    head=['empno','company','emp name']
    val=[{'empno':'1','emp name':'sree','company':'cognizent'},
         {'empno':'2','emp name':'joshna','company':'wipro'},
         {'empno':'3','emp name':'divya','company':'capgemini'}]
    obj=csv.DictWriter(fp,fieldnames=head)
    obj.writeheader()
    obj.writerows(val)