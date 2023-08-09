# python program to access environment variables
import os


# to print all env.variables
# for key, value in os.environ.items():
#     print('{}: {}'.format(key, value))

# Enter env.variable to get its value

KEY = input()
KEY = KEY.upper()
KEY = KEY
print(KEY)
print(os.environ[KEY]) 
