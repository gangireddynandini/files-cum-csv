try:
    a=open('nandu.py','a')
    a.write('tq dear \n')
    a.write('good morning \n')
    a.write('have a nice day \n')
    print('data writen to the file ')
    print('is file closed:',a.closed)
except FileExistsError:
    print('this file alrad exists')
finally:
    print('is file closed:',a.closed)
    a.close()
    print('is file closed after manual close',a.closed)
    print('thnx for using this program')