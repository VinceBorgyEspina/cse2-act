def copy_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file_in:
            content = file_in.read()
        
        with open(output_file, 'w') as file_out:
            file_out.write(content)
        
        print("File copied successfully!")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except PermissionError:
        print(f"Permission denied to access file '{input_file}' or create file '{output_file}'.")

# Example usage:
if __name__ == "__main__":
    copy_file("input.txt", "output.txt")
