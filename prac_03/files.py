""" File reading for Prc_03 """

name = input("Name: ")
out_file = open("name.txt","w")
print(name, file=out_file)
out_file.close()


in_file = open("name.txt")
text = in_file.read().strip()
out_file.close()
print(f"Hi {text}!")

