
def primeNumbers(num): #function declaration
    
    x = [2] 
    begin = 3 
    while True:
        for i in range(3, int(begin**0.5) + 1):  
            if begin % i == 0 or begin % 2 == 0: 
                break
        else:
            x.append(begin) #append the number thats not divisible by 
        begin += 1
        if begin == num:
            break
            
    return x #return list of prime numbers


print primeNumbers(80)