filename = "sample.txt"

try:
    with open(filename,"r") as file:
        for line in file:
          print("reading file content",line.strip())
except FileNotFoundError:
    print(f"Error: The File '{filename}' does not exist")

