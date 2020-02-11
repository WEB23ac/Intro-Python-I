import time

num = input('Provide a number ~~>')


def check_prime(num):
    start_time = time.time()

    num = int(num)
    if num == 2:
        response = 'Number is Prrime'
    # create array of integers 2-num
    if num % 2 == 0:
        response = 'Number is Not Prime.'
    elif num % 3 == 0:
        response = 'Number is Not Prime.'
    elif num % 5 == 0:
        response = 'Number is Not Prime'
    elif num % 7 == 0:
        response = 'Number is Not Prime'
    else:
        response = 'Number is Prime'
    # create list called non_prime, add every 2nd entry to list
    print(response, 'calculated in %s seconds' % (time.time() - start_time))


check_prime(num)
