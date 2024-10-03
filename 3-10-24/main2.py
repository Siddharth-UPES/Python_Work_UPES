# write a function to count n and evaluate a=n*10 for all values from 0 to n
import time

def count(n):
    for i in range(0,n):
        a=n*10

n=100000

def wrapper(func ,*args,**kwargs): #generalize
    def wrapped(*args,**kwargs):
        start_time= time.time() *1000000
        func(*args,**kwargs)# timinig this function call /execution
        end_time= time.time() *100000
        print(f"\n n={n} Time to execute is {end_time-start_time} micro second")

    #wrapper(*args ,**kwargs)
    return wrapped


@wrapper#decorator
def count(n):
    for i in range(0,n):
        a=n*10

count(n)
@wrapper
def random():
    pass


random()
# #wrapper(count,n)
# #wrapped_function=wrapper(count,n)
# wrapped_count=wrapper(count,n)
# wrapped_count(n)