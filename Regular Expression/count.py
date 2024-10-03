# def outer_function(message):
#     #value of message is present here
#     def inner_function():
#         print(message)
#         #inner_function()
#     return inner_function
# closure =outer_function("Hello from closure")

# closure()


def counter():
    count =0
    def increment():
        nonlocal count
        count +=1
        print(count)

    return increment

c1=counter()
c1() #1
c1() #2

c2=counter()

c2() #1
c1() #3
