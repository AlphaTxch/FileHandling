# 15/12/22 

myFile = open("book.txt","r")
fileContents = myFile.read()
print(fileContents)
x = 0 

for letter in fileContents:
       if letter == "\n":
        x = x + 1
        print(x) #letter count 


for line in fileContents:
    splitLine=line.split(" ")
    x+=len(splitLine)
    print(splitLine)
    print(len(splitLine))
    input # to manually create an input enter into the command before proceeding 
input() # if you want it automated 

print(x)




