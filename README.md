
# File Organizer

A Python command-line tool that automatically organizes files in a folder into categories such as Images, Documents, Videos, Audio, Archives, and Code.

## Why this project?

Manual file organization is repetitive and time-consuming. This tool automates the process and demonstrates practical IT automation skills.

## Features

- Organizes files by extension
- Creates category folders automatically
- Handles unknown file types using an `Others` folder
- Simple command-line interface

## How to run

```bash
python file_organizer.py
```

## Example

```text
Enter folder path to organize: /Users/yourname/Downloads

Moved: photo.jpg -> Images
Moved: report.pdf -> Documents
Moved: setup.zip -> Archives

Done. 3 files organized.
```

## What I learned

- Working with the `os` and `shutil` modules
- File paths and extensions
- Creating folders automatically
- Writing reusable Python functions
