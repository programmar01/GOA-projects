def is_prime(number):
    if number <= 1:
        return False
    elif number <= 5 and number != 4 and number != 2:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    firstnum = 5
    while firstnum * firstnum <= number:
        if number %firstnum == 0 or number % (firstnum + 2) == 0:
            return False
        firstnum += 6
    return True


def backwards_prime(start, stop):
    result = []
    for i in range(start, stop + 1):
        reversed_i = int(str(i)[::-1])
        if (is_prime(i) and is_prime(reversed_i)) and i != reversed_i:
            result.append(i)