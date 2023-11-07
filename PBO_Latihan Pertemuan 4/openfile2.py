# open a file
file1 = open("contoh.txt", "r")
teks="latihan Python\n"

file2 = open("contoh.txt", "a")
file2.write(teks)
file2.close()

# read the file
read_content = file1.read()
print(read_content)

# close the file
file1.close()