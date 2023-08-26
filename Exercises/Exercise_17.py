# script to write string to a file after creating it

def main():
    ls = ["Practice", " alot", " results", " in",
          " less", " mistakes", "\n", "FOCUS"]
    fd = open('txtFile_EX17.txt', 'w')
    fd.write("".join(ls))


main()
f = open('txtFile_EX17.txt', 'r')
print(f.read())
