fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('Cannot open file: ' + fname)
    exit()    

spam_cnt = 0
confidence_sum = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        spam_cnt += 1
        confidence_num = float(line.split(': ')[-1].rstrip())
        confidence_sum += confidence_num
        # print(confidence_num)
        
confidence_avg = confidence_sum / spam_cnt
print('Average spam confidence: ' + str(confidence_avg))