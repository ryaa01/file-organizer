import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    moved_files = 0

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()
            destination_folder = "Others"

            for folder, extensions in FILE_TYPES.items():
                if extension in extensions:
                    destination_folder = folder
                    break

            destination_path = os.path.join(folder_path, destination_folder)
            os.makedirs(destination_path, exist_ok=True)

            shutil.move(file_path, os.path.join(destination_path, file_name))
            moved_files += 1
            print(f"Moved: {file_name} -> {destination_folder}")

    print(f"\nDone. {moved_files} files organized.")

def main():
    folder = input("Enter folder path to organize: ")
    organize_files(folder)

if __name__ == "__main__":
    main()
