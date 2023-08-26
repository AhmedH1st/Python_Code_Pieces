# script to get the number of lines&words in a file

with open('txtFile_EX16.txt', 'r') as f:
    lines = f.readlines()
    words = ''
    words = words.join(lines)
    print(len(lines))
    print(len(words.split()))
