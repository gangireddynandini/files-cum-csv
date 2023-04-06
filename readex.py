try:
    filename=input('enter file name:')
    with open(filename)as fp:
       k=fp.read()
       print(k)
       print('-'*20)
except FileNotFoundError:
    print('not exists')

