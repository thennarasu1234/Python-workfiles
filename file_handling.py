file_1=open("sample.txt")
file_1.close()

file_1=open("sample.txt","r")
read=file_1.read()
file_1.readline
print(read)

file_2=open("sample1.txt","w")
file_2.write("Hey buddy")
# file_1.readline
file_2.close()

file_3=open("sample1.txt","a")
file_3.write("nirmal")
file_3.close()


with open("sample1.txt","r") as F:
    F.readline()
