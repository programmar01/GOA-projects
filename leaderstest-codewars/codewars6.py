def dig_pow(n, p):
    sum = 0
    for i in list(str(n)):
        sum += int(i) ** p
        p += 1
    
    if sum % n == 0:
        return int(sum / n)
    return -1