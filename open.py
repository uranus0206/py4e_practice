fhand = open('mbox-short.txt')

count = 0
for line in fhand:
    count = count + 1

print('Line Count: %d' % count)

###

fhand.seek(0)
inp = fhand.read()
print(len(inp))

print(inp[:20])

fhand.close()

###