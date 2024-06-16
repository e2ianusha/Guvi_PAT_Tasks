import datetime

def create_text_file_with_timestamp():
    # Generate current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a file with timestamp as the name
    file_name = f"{current_time}.txt"
    with open(file_name, 'w') as file:
        file.write(current_time)
    
    print(f"Text file '{file_name}' created with content: {current_time}")

# Example usage:
create_text_file_with_timestamp()