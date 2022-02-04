def read_file():
    file = open("Demo.txt","r")
    for line in file:
        print(line, end="")
read_file()
