prompt = "Enter a number: "
count = 0
total = 0
average = 0
num_list = []

def readNumber(in_var):
    global count
    global total
    global average
    
    count = count + 1
    total = total + in_var
    average = total / count

def find_max_value_in_list(num_list):
    max_num = None
    for value in num_list:
        if max_num is None or value > max_num:
            max_num = value
            
    return max_num

def find_min_value_in_list(num_list):
    min_num = None
    for value in num_list:
        if min_num is None or value < min_num:
            min_num = value
            
    return min_num


while True:
    input_var = input(prompt)
    
    try:
        number = float(input_var)
        num_list.append(number)
        readNumber(number)
        
    except Exception as e:
        if input_var == "done":
            print("%d %f %f" % (total, count, average))
            print("Max: %d" % find_max_value_in_list(num_list))
            print("min: %d" % find_min_value_in_list(num_list))
            break
        
        print("Invalid input")
