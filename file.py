import sys, os, json

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_text(path):
    file = "".join(get_file(current_directory + "/" + path))
    if not file:
        print("Failed to get text"), sys.exit(1)

    return file


def get_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def add_entry_to_file(file_path, data):
    with open(file_path, "a") as file:
        file.write(json.dumps(data) + "\n")
    print(f"Successfully added data to {file_path}")


def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully")
    except OSError as error:
        print(f"Directory '{path}' cannot be created. Error: {error}")
