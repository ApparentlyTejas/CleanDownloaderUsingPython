# 🧹 Clean My Downloads

A Python script to automatically organize and clean your **Downloads folder** by:

- Sorting files into folders based on type (Images, Documents, Videos, etc.)
- Removing `.exe` files (optional cleanup of installers)
- Detecting and removing duplicate files by comparing their contents
- Logging every action for transparency

---

## 📂 How It Works

This script scans your `~/Downloads` folder and:

1. Deletes any `.exe` files to free up space
2. Sorts files into type-based folders in your home directory:
   - `Images/`
   - `Documents/`
   - `Videos/`
   - `Music/`
   - `Archives/`
   - `Others/` (for uncategorized files)
3. Finds duplicate files (with identical content) and keeps only the **latest version**

---

## 🚀 Features

- ✅ Automatically organizes by file type
- 🗑️ Deletes `.exe` files safely
- 🔍 Finds duplicates using full file comparison (`filecmp`)
- 🧠 Keeps your newest file version
- 📝 Logs actions with timestamps using Python's `logging` module

---

## 📦 Requirements

- Python 3.6 or newer  
- Works on macOS, Linux, and Windows  
- No external libraries required (uses only the Python standard library)

---

## ▶️ Usage

1. Clone this repository:

```bash
git clone https://github.com/ApparentlyTejas/ProjectsInPython.git
cd ProjectsInPython
python cleanDownloader.py
🧠 Customization
You can change the behavior by editing the script:

File types → Modify the file_type_folders dictionary in main()

Number of duplicates → Currently deletes all but the newest

Safety → You could add a dry-run mode or confirmation prompts


## 🙋‍♂️ Author
Tejas Malhotra
Automation enthusiast.
Follow me or contribute at github.com/ApparentlyTejas
