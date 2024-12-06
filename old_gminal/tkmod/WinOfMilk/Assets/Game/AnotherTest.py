from os import read


def main():
    #Open the file back and read the contents
    f=open("level.txt", read)
    if f.mode == 'r':
       contents =f.read()
    print (contents)
if __name__== "__main__":
    main()
