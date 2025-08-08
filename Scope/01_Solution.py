# x = "global"       # Global scope

# def outer():
#     x = "enclosed"  # Enclosed scope
#     def inner():
#         x = "local"     # Local scope
#         print(x)
#     inner()

# outer()


# username = "chai"
# def add():
#     username = "code"
#     print(username)
# print(username)
# add()

# x = 88

# def add():
#     x = 99
#     def sub():
#         x = 12
#         print(x)
#     sub()   
#     print(x)
    
    
# print(x)
# add()

def add(abs):
    def sub():
        print("Hello",abs)
    return sub
    
my_call = add("Hello")

my_call()