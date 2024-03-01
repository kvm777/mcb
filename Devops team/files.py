import os

def list_of_files(foler_path):
    try:
        paths_folders = foler_path.split()
        # print(paths_folders)
        files_folder = []
        for path in paths_folders:
            folder = os.listdir(path)
            files_folder.append(folder)
            # print(files_folder)
        return files_folder, None
    except FileNotFoundError:
        return None, "files not found"
    except PermissionError:
        return None, "permission Denied"
    

def main():
    folders_path = input("enter the folders path: ")
    folders, error_message = list_of_files(folders_path)
    if folders:
        for folder in folders:
            print(f"files in folder {folder}")
            for file in folder:
                print(file)
    else:
        print(error_message)


if __name__ == "__main__":
    main()
