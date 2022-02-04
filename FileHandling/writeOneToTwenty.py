def main(): 
 obj1=open("WriteNumbers.txt","w") 
 for x in range (1,21): #Iterates from 1 to 20  
     x=str(x) #Convert number to string  
     obj1.write(x) #Write number to a output file  
     obj1.write(" ") #Space to separate Numbers   
main() 
file = open("WriteNumbers.txt","r") 
for line in file: 
 print(line, end="") 
file.close() 
