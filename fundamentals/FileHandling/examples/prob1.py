# Step 1: (Run once) Create and write into the file
with open("sample.txt", "w") as f:
    f.write("Python is powerful\n")
    f.write("File handling is important\n")
    f.write("Practice makes perfect\n")


# Step 2: Read and count
with open("sample.txt", "r") as f:
    content = f.read()

# Count lines
lines = content.split("\n")
line_count = len(lines)

# Count words
words = content.split()
word_count = len(words)

# Count characters (including spaces and newline)
char_count = len(content)

print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", char_count)