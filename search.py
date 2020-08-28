fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
#    # Skip 'ininteresting lines'
#    if not line.startswith("From:"):
#        continue
#    # Process interesting line
#    print(line)

    if line.find('@uct.ac.za') == -1:
        continue
    print(line)