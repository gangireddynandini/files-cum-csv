try:
    with open('baby.py','a')as fp:
        print('position of fp:',fp.tell())
        fp.write('file opened succesfully \n')
        fp.write('welcome to this beautiful world \n')
        print('position of fp:',fp.tell())
        print('is file close:',fp.closed)
    print('is file close:',fp.closed)
except FileNotFoundError:
    print('file not found')
