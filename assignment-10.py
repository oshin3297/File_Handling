#Question1:->Write a Python program to read n lines of a file.

f=open('file1.txt','r')
file=f.read()
print(file)
f.close()
print()


#Question2:->Write a Python program to count the frequency of words in a file.

f=open("file1.txt",'r')
data=f.read()
words=data.split()
dict={}
for i in words:
    dict[i]=words.count(i)
print(dict)
print()


#Question3:->Write a Python program to copy the contents of a file to another file.

f=open("file1.txt",'r')
g=open("file2.txt",'w')
for i in f:
    g.write(i)
f.close()
g.close()
print()


#Question4:->Write a Python program to combine each line from first file with the corresponding line in second file.

f1=open("file1.txt",'r')
f2=open("file3.txt",'r')
for i1,i2 in zip(f1,f2):
    f3=open("file5.txt",'a')
    f3.write(i1+i2)
    f3.close()
f2.close()
f1.close()
print()


#Question5:->Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.

f5=open('file1.txt')
temp=open('file4.txt','w+')
sor=f5.readlines()
sor.sort()
temp.write(str(sor))
temp.seek(0)
output=temp.read()
print(output)
print()
