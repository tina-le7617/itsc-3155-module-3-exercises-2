'''
https://stackoverflow.com/questions/12444004/how-long-does-my-python-application-take-to-run
https://www.youtube.com/watch?v=Qk0zUZW-U_M
'''

import time

# Use time() method from time module to keep track of program's starting time
start_time = time.time()

def fibonacci(n):

    # Always return 1 if it's the 1st term
    if n == 1:
        return 1
    
    # Always return 1 if it's the 2nd term
    elif n == 2:
        return 1

    # If the term is larger than 2nd term > Keep calling the function itself (recursion)
    # Returning the sum of two previous two terms
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

n = 35
print(f'fibonacci({n})={fibonacci(n)}')
print(f'fibonacci({n}) took {time.time() - start_time} seconds')