# main file 

x=10 #global variable


def outer_function():
    x=20 #enclosing variable
    def inner_function():
        x=30 #local variable
        print(x) #output: 30
    inner_function()
    print(x) #output: 20

outer_function()
print(x) #output:10