celsius_prompt = 'Enter Celsisus: '
celsius = input(celsius_prompt)

fahrenheit = (float(celsius) * (9/5)) + 32
print('Farenheit: ' + str(fahrenheit))