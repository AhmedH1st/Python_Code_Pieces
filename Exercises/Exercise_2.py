# test whether a passed letter is a vowel or not.

ch = input()
if (ch.lower() == 'a' or ch.lower() == 'u' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'y'):
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
