f = open("./python_fileupload/english.txt", "rb")
data = f.read()
print(data)

f = open("./python_fileupload/korean.txt", "rb")
data2 = f.read()
data3 = data2.decode('utf-8')
print(data2)
print(data3)
