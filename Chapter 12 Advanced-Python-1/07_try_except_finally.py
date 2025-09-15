try:
    a = int(input("Enter any number:"))

except Exception as e:
    print(e)

finally:
    print("I am inside of finally")

# final block main use in functions