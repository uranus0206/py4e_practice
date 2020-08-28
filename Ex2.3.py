hour_prompt = 'Enter Hour: '
rate_prompt = 'Enter Rate: '
err_msg = 'Error, please enter numeric input.'

try:
    hour = float(input(hour_prompt))
    rate = float(input(rate_prompt))
except:
    print(err_msg)
    exit()

hour_ceil = 40
addition_hour = hour - hour_ceil
addition_factor = 1

if addition_hour > 0:
    addition_factor = 1.5    
    pay = (hour_ceil * rate) + (addition_hour * (rate * addition_factor))
else:
    pay = (hour * rate)


print('Pay: ' + str(pay))
