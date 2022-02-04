def main(): 
 obj1= open("Demo1.txt","w") 
 obj1.write("Hello, How are you?\n") 
 obj1.write("Welcome to the chapter File Handling.\n") 
 obj1.write("Enjoy the session.\n") 
main() 
file = open("Demo1.txt","r") 
for line in file: 
 print(line, end="") 
file.close() 
