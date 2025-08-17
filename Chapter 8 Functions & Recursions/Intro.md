# Function --> A function is a group of statements performing a specific task.

    - Built-In Functions :-
            1. Input / Output -
                print() → Displays output.
                input() → Takes input from the user.

            2. Data Type Conversion -
                int() → Converts to integer.
                float() → Converts to floating-point number.
                str() → Converts to string.
                bool() → Converts to True or False.
                list(), tuple(), set(), dict() → Converts data into respective data types.

            3. Mathematical Operations -
                abs(x) → Absolute value.
                pow(a, b) → a raised to the power of b.
                round(x) → Rounds a number.
                max() / min() → Finds largest / smallest value.
                sum() → Adds up elements in an iterable.

            4. Sequence Operations -
                len() → Returns length of a sequence.
                sorted() → Returns sorted list.
                reversed() → Returns reversed iterator.
                enumerate() → Returns index + value while looping.
                range() → Generates a sequence of numbers.

            5. Utility Functions -
                type() → Shows the type of an object.
                id() → Returns unique ID of an object.
                help() → Shows help documentation.
                dir() → Lists available attributes and methods.

                # Using some built-in functions
                    name = input("Enter your name: ")  # input
                    print("Hello", name)               # print
                    nums = [10, 20, 30]
                    print("Sum:", sum(nums))           # sum
                    print("Max:", max(nums))           # max
                    print("Type of nums:", type(nums)) # type 

# Functions with Arguments -->
    - A function can accept some value it can work with. We can put these values in parentheses.
        ex.,
            def greet(name,ending): # name is a parameter(argument).
                print("Good Day,"+ name)

                greet("SuniL")

# Recursion -->
        Recution is a function which calls itself.
        It is used to direcly use a mathemalical formula as a function. 
        for exampble
        factorial (n) = n x factorial (n-1)
        This funtion can be defined as follows -
        def factorial (n):
            if i==o ou i==1: # Base condition which does't call the function any further.
                return 1
            else:
            return n* tactorial (n-1) → function calling itself
        This works as follows:
            Factoual (4) #  Funchon calledo
                4x Factorial(3)
                4x [3 x factorial (2)]
                4 x 3 x[2 x factorial(1) function returned]
       
                The programmer need to be extremely Careful while working with recursion to ensure that the function does't infinity keep calling itself.
                Recursion is sometimes the most direct way to code an alogorithm.
                