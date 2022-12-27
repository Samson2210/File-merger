import os

srcPath = input("Enter the path:   ")    #Path
files = os.listdir(srcPath)
print('Total files:',len(files)-1)

#removing the files.py file from the list
try:
    files.remove('files.py')
except:
    print("File does not exists")

#setting the output file
outputfile = input('Enter the output file name along with the extention:  ')
f = open(outputfile,'x')            #creating the outfile
f.close()

#appending the contents of files to the outputfile
print("--------------Processing------------")
try:
    for file in files:
        with open(file,'r') as f, open(outputfile,'a') as second:
            for line in f:
                second.write(line)
            second.write("\n\n");    
except:
    print("Some error occured")
second.close()
f.close()

print("Finished")