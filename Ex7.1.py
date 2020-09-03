fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot open file: ' + fname)
    exit()    

for line in fhand:
    print(line.upper())