prompt = 'Please enter score range from 0.0 to 1.0. Or "quit" to exit: '

def score_convert(in_value):
    try:
        score = float(in_value)
    except:
        print('Bad score.')
        return
    
    if score < 0.6:
        print('F')
    elif score >= 0.6 and score < 0.7:
        print('D')
    elif score >= 0.7 and score < 0.8:
        print('C')
    elif score >= 0.8 and score < 0.9:
        print('B')
    elif score >= 0.9 and score < 1.0:
        print('A')
    else:
        print('Bad score')
    
while 1:
    in_value = input(prompt)
    
    if in_value == 'quit':
        exit()
        
    score_convert(in_value)
