print("open and close file")
text_file=open("read_it.txt","r")
data = []
with open("read_it.txt","r") as f:
    data = f.readlines()
for i in range(0,9):
    print(data[i])
    

