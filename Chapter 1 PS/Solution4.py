# import os

# def list_directory_contents(path='.'):
#     """
#     Prints all entries (files and directories) in the given path.
#     Defaults to current directory if no path is provided.
#     """
#     try:
#         entries = os.listdir(path)  # gets all files & directories :contentReference[oaicite:1]{index=1}
#     except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
#         print(f"Error accessing {path}: {e}")
#         return

#     print(f"Contents of directory '{path}':")
#     for entry in entries:
#         print(entry)

# if __name__ == '__main__':
#     directory = input("Enter directory path (leave empty for current): ").strip() or '.'
#     list_directory_contents(directory)