try:
    h=open('groupbyex1.py','w')
    print('file opened')
    print('type of fp:',type(h))
    t=(15,'joshna',67,'india')
    h.writelines(str(t))
    print('data writen to the file')
    print('is file readablr:',h.readable())
    print('is file readablr:',h.writable())
    print('file mode',h.mode)

except FileNotFoundError:
    print('file not found')


