#!/usr/bin/env python3
"""
file_manager.py
Python File Management and Data Processing Utility

Implements:
 - TASK1: Project Initialization
 - TASK2: File creation and writing
 - TASK3: Reading and file info
 - TASK4: Backup and archiving
 - TASK5: Logging system
 - TASK6: Advanced file operations (delete)
"""

import os
import sys
import shutil
from datetime import datetime
import traceback

# Constants
STUDENT_FOLDER = "StudentFiles"
LOG_FILENAME = "activity_log.txt"

def log_message(message, folder=STUDENT_FOLDER):
    """Append a timestamped message to activity_log.txt inside StudentFiles."""
    try:
        if not os.path.exists(folder):
            # If folder missing, create it (safe-guard)
            os.makedirs(folder)
        log_path = os.path.join(folder, LOG_FILENAME)
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")  # FIXED: Added space
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} {message}\n")
    except Exception as e:
        # If logging itself fails, print to stderr (we avoid crashing silently)
        print("Failed to write log:", e, file=sys.stderr)

def initialize_folder():
    """TASK1: Check/create StudentFiles and show absolute path."""
    try:
        if not os.path.exists(STUDENT_FOLDER):
            os.mkdir(STUDENT_FOLDER)
            print(f"Created folder: {os.path.abspath(STUDENT_FOLDER)}")
        else:
            print(f"Folder already exists: {os.path.abspath(STUDENT_FOLDER)}")
    except Exception as e:
        # Terminate gracefully with message if folder creation fails
        print("Error creating folder:", e, file=sys.stderr)
        log_message(f"ERROR: Failed to create folder: {e}")
        sys.exit(1)

def task2_create_file():
    """TASK2: Create date-based filename and write five student names."""
    date_str = datetime.now().date().isoformat()  # e.g., 2025-10-31
    filename = f"records_{date_str}.txt"
    path = os.path.join(STUDENT_FOLDER, filename)

    try:
        print("Enter five student names. Press Enter after each name.")
        names = []
        for i in range(1, 6):
            name = input(f"Student {i} name: ").strip()
            # Allow empty input but record as empty string if user presses Enter
            names.append(name)

        with open(path, "w", encoding="utf-8") as f:
            for name in names:
                f.write(name + "\n")

        created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Success: {filename} created at {created_time}")
        return filename
    except Exception as e:
        print("Error creating/writing file:", e, file=sys.stderr)
        log_message(f"ERROR: Failed to create/write {filename}: {e}")
        raise

def task3_read_and_info(filename):
    """TASK3: Read file contents, show size and last modified date."""
    path = os.path.join(STUDENT_FOLDER, filename)
    try:
        print("\n--- File contents ---")
        with open(path, "r", encoding="utf-8") as f:
            contents = f.read()
            print(contents.rstrip("\n"))
        size = os.path.getsize(path)
        mtime = os.path.getmtime(path)
        last_modified = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
        print(f"Size: {size} bytes")
        print(f"Last modified: {last_modified}")
    except Exception as e:
        print("Error reading file/info:", e, file=sys.stderr)
        log_message(f"ERROR: Failed to read {filename}: {e}")
        raise

def task4_backup_and_archive(filename):
    """TASK4: Make a backup copy, create Archive subfolder, move backup there, list files."""
    date_str = datetime.now().date().isoformat()
    src_path = os.path.join(STUDENT_FOLDER, filename)
    backup_name = f"backup_{filename}"
    backup_path = os.path.join(STUDENT_FOLDER, backup_name)
    archive_folder = os.path.join(STUDENT_FOLDER, "Archive")

    try:
        # a) copy
        shutil.copy(src_path, backup_path)
        print(f"Backup created: {backup_name}")

        # b) create Archive subfolder if not exists
        if not os.path.exists(archive_folder):
            os.mkdir(archive_folder)

        # c) move backup into Archive
        moved_path = shutil.move(backup_path, archive_folder)
        print(f"Backup moved to Archive: {moved_path}")

        # d) list files in Archive
        archive_files = os.listdir(archive_folder)
        print("\nFiles in Archive folder:")
        for f in archive_files:
            print("-", f)

        return backup_name, archive_folder
    except Exception as e:
        print("Error during backup/archive:", e, file=sys.stderr)
        log_message(f"ERROR: Backup/archive failed for {filename}: {e}")
        raise

def task5_log_success(filename):
    """TASK5: Append success entry to activity_log.txt"""
    try:
        log_message(f"{filename} created and archived successfully.")
    except Exception as e:
        print("Logging failed:", e, file=sys.stderr)

def task6_delete_file():
    """TASK6: Ask user if they want to delete a file, delete and log if confirmed."""
    try:
        choice = input("\nWould you like to delete a file from StudentFiles? Type 'Yes' to confirm: ").strip()
        if choice.lower() == "yes":
            fname = input("Enter the exact filename to delete (e.g., records_2025-10-31.txt): ").strip()
            target_path = os.path.join(STUDENT_FOLDER, fname)
            if os.path.exists(target_path):
                os.remove(target_path)
                print(f"{fname} has been deleted.")
                log_message(f"{fname} deleted by user.")
            else:
                print("File not found:", fname)
                log_message(f"Attempted delete failed - file not found: {fname}")
        else:
            print("Delete step skipped.")
    except Exception as e:
        print("Error during delete operation:", e, file=sys.stderr)
        log_message(f"ERROR: Delete operation failed: {e}")

def main():
    try:
        initialize_folder()                # TASK1
        filename = task2_create_file()     # TASK2
        task3_read_and_info(filename)      # TASK3
        backup_name, archive_folder = task4_backup_and_archive(filename)  # TASK4
        task5_log_success(filename)        # TASK5
        task6_delete_file()                # TASK6

        # After everything, display remaining files in StudentFiles
        print("\nRemaining files in StudentFiles:")
        for f in os.listdir(STUDENT_FOLDER):
            print("-", f)

    except Exception as e:
        # A last resort catch; all errors should be logged earlier
        print("A critical error occurred. Check activity_log.txt for details.", file=sys.stderr)
        log_message(f"CRITICAL: {traceback.format_exc()}")

if __name__ == "__main__":
    main()