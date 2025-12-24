try:
    # Attempt to open and read the file line by line
    with open("sample.txt", "r") as file:
        for line in file:
            # strip() removes the extra newline character from each line
            print(line.strip())

except FileNotFoundError:
    # Error handling if the file is missing
    print("Error: The file 'sample.txt' was not found.")

except Exception as e:
    # General error handling for other potential issues (e.g., permissions)
    print(f"An unexpected error occurred: {e}")








