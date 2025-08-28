# File Read & Write with Error Handling

def main():
    # Ask the user for input file
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: make everything uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
