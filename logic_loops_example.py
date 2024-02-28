"""
This script will show how to use logical tests (if statements),
for loops, and imports.
"""

#%% imports

import os

print(os.getcwd())

print(os.listdir())

#%% if example
# a = 'test'
a = None

if a:
    print("The variable a is", a)

# for loop example
for i in range(10):
    print(f'The value of i is {i}')

    # nested for loop
    for j in range(2):
        print(f'i is {i}, j is {j}')

# %% look at files in the folder
file_list = os.listdir()


for file in file_list:
    print(f'The current file is {file}')

    if file.endswith('.py'):
        print(f'{file} is a python file.')
    elif file.endswith('.sh'):
        print(f'{file} is a shell script.')


# %%
