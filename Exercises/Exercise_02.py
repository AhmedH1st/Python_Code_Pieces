# test whether a passed letter is a vowel or not.

ch = input()
ch = ch.lower()
if (ch == 'a' or ch == 'u' or ch == 'i' or ch == 'o' or ch == 'y'):
    print("VOWEL")
else:
    print("CONSTANT")


# Another Solution

# def isvowel(ch):
#     str = 'aiuoy'
#     ch = ch.lower()
#     return (str.find(ch) != -1)


# ch = input()
# print(isvowel(ch))

