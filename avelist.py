numlist = list()

while True:
    inp = input('Enter a num: ')
    if inp == 'done': break
    
    val = float(inp)
    numlist.append(val)
    
avg = sum(numlist) / len(numlist)
print('Average: ', avg)