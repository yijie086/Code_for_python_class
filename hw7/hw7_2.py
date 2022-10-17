print("This is a python code for homework7-2: Read and Write")
f = open("hw7_2_READ_DAT.txt", encoding="utf-8")
temp = f.read()
f.close()

f = open("hw7_2_WRITE_DAT.txt", mode="w", encoding="utf-8")
f.write(temp)
f.close()
