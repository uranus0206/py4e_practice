str = 'X-DSPAM-Confidence: 0.8475 '

colon_idx = str.find(':')
float_str = str[colon_idx+1 : ].strip()
number_float = float(float_str)
print('Number: %g' % number_float)
