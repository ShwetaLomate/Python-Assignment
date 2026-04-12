# Writing
with open("myfile.txt", "w") as file:
    file.write("Hello, this is the first line.\n")

# Appending
with open("myfile.txt", "a") as file:
    file.write("Appended line.\n")

# Reading
with open("myfile.txt", "r") as file:
    print(file.read())