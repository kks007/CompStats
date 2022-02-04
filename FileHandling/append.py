fp1=open('Demo.txt','a') 
#Open file in append mode 
fp1.write('\nWow, Cannot believe.') 
#Append contents to a file 
file = open("Demo.txt","r") 
for line in file:
 print(line, end="") 
file.close() 
