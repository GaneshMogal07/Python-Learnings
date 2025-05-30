import os

# 1. Create a new file and write initial content
print("1. Creating and writing to file...")
with open("sample.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

# 2. Read the file content
print("\n2. Reading the file content...")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 3. Append more content to the file
print("3. Appending to the file...")
with open("sample.txt", "a") as file:
    file.write("This is the third line (appended).\n")

# 4. Read again to verify appended content
print("\n4. Reading after append...")
with open("sample.txt", "r") as file:
    print(file.read())

# 5. Delete the file
print("5. Deleting the file...")
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
