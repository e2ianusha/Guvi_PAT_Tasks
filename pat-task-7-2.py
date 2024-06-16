def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}': {content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Example usage:
file_to_read = input("Enter the name of the text file to read (e.g., 2024-06-16_15-30-00.txt): ")
read_text_file(file_to_read)
