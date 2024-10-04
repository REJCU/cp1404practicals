""" File reading for Prc_03 """

# 1.
name = input("Name: ")
out_file = open("name.txt","w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt")
text = in_file.read().strip()
out_file.close()
print(f"Hi {text}!")

# 3.
with open("numbers.txt", "r") as number_files:
    number_1 = int(number_files.readline())
    number_2 = int(number_files.readline())
    print(number_1 + number_2)

# 4.
with open("numbers.txt", "r") as number_in_file:
    for line in number_in_file:
        number = line.strip()
        print(number)
