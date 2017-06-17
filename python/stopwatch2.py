import time

def time_execution(code):
    start_time = time.clock()
    result = eval(code)
    run_time = time.clock() - start_time
    return result , run_time


def spin_loop(n):
    i = 0
    while i<n:
        i=i+1

print (time_execution('spin_loop(100)'))
print (time_execution('spin_loop(1000)'))
print (time_execution('spin_loop(10000)'))
print (time_execution('spin_loop(100000)'))
print (time_execution('spin_loop(10  ** 5)'))
print (time_execution('spin_loop(10 ** 6)'))
print (time_execution('spin_loop(10 ** 9)'))
