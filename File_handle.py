# # create file handle
# file =open("push command.txt","r")
# content=file.read()
# print(content)
# file.close()


#write a file handle
# file=open("example.txt","w")

# file.write("\n new test file is there".upper())
# file.close()



# #using the loop

# filename="example.txt"
# file=open(filename,"r")

# fileContent = file.readlines()
# file.close()

# for line in fileContent:
#     print(line)


filename="read_text.csv"
file=open(filename,"r")
fileContent=file.read
file.close()

rows=fileContent.split("\n")
for row in rows:
    print(f"rows is {row}")
    cols =row.split(",")
    for col in cols:
        print(col)