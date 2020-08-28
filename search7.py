fname = input('Enter the file nsme: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
        
print('There were', count, 'subject lines in', fname)