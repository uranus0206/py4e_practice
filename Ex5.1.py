prompt = "Enter a number: "
count = 0
total = 0
average = 0

def readNumber(in_var):
    global count
    global total
    global average
    
    count = count + 1
    total = total + in_var
    average = total / count

while True:
    input_var = input(prompt)
    
    try:
        number = float(input_var)
        readNumber(number)
        
    except Exception as e:
        if input_var == "done":
            print("%d %f %f" % (total, count, average))
            break
        
        print("Invalid input")