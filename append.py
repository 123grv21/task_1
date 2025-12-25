filename = "output.txt"

# Take user input
value = input("Enter a value: ")

# Write data to file
with open(filename, "w") as file:
    file.write(value + "\n")

print("Data written to file successfully.")

# Append additional data
with open(filename, "a") as file:
    file.write("Additional data appended.\n")

print("Data appended to file successfully.")

# Read and display final content
print("\nFinal file content:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
