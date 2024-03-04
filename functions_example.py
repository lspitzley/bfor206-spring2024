"""
This file will contain some example functions
to demonstrate how functions work.
"""

#%% imports

#%% functions

def new_function():
    """
    This function is empty. The pass keyword
    is required, otherwise you'll get an error.
    """
    pass

def func2(arg1):
    """
    This function prints out the argument.
    """

    print(f'The value of arg1 is {arg1}')

def func3(arg1, arg2=True):
    """
    This function has two arguments. 
    arg1 is required, arg2 is optional.
    """

    if arg2:
        print("arg2 is True")
    
    # print(f'arg1 is {arg1}')
    # use func2 to print
    func2(arg1)

def add_numbers(a, b):
    """
    Adds two numbers together.

    Returns the sum.
    """

    # do some basic error checking
    for number in [a, b]:
        if not isinstance(number, (int, float)):
            raise ValueError(f'Received a non-numeric value: {number}')

    sum = a + b
    return sum
    
#%% run the functions

# run new_function 
new_function()

# run func 2
func2(10)

# run func3 with one argument
func3("Hello World")
# change arg2 to False
func3("Test", False)
# using names when calling
func3(arg2=False, arg1="one")

#%% calling add_numbers
sum = add_numbers(3, 4)
print(f"The sum is {sum}")

sum2 = add_numbers('a', 3)

#%% basic testing
assert add_numbers(3, 4) == 7
assert add_numbers(-1, 1) == 0
assert add_numbers(1.2, 3.4) == 4.6

# %%
