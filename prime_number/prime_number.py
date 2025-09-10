def detect_pn(number:int):
    if number <= 1:
        return False
    

    for i in range(2,number):
        if number % i == 0:
            return False    
    return True

        

val = detect_pn(9)
print(val)

