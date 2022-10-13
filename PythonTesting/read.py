#How to read text file content using python

file=open('E:\pro.txt')          #open the file

#print(file.read(2))             #read the n number of character by passing parameter

#print(file.read())              #read method read all the content in file

#print(file.readline())         #readline method read the content line by line
#print(file.readline())



#print line by line using readline method

line= file.readline()
while line !="":
    print(line)
    line=file.readline()

