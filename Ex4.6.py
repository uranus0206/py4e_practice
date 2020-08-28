def computepay(hour, rate):
    hour_ceil = 40
    addition_hour = hour - hour_ceil
    addition_factor = 1

    if addition_hour > 0:
        addition_factor = 1.5    
        pay = (hour_ceil * rate) + (addition_hour * (rate * addition_factor))
    else:
        pay = (hour * rate)
        
    return pay

hour_prompt = 'Enter Hour: '
rate_prompt = 'Enter Rate: '
err_msg = 'Error, please enter numeric input.'

try:
    hour = float(input(hour_prompt))
    rate = float(input(rate_prompt))
    
    print('Pay: ' + str(computepay(hour, rate)))    
except:
    print(err_msg)
    exit()


