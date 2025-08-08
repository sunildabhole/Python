def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name ="Sunil",age = 21)
print_kwargs(name ="Sahil",age = 21, village ="Saroli")
print_kwargs(name ="Prabhu",age = 18, height =136)