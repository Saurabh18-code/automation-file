# 📁 File Automation System

A Python-based File Automation System that automates common file management tasks such as creating files, reading text files, processing CSV data, moving and renaming files, and generating log files. This project demonstrates file handling, exception handling, logging, and automation using Python.

---

## 📌 Features

- 📂 Creates a demo directory automatically
- 📄 Generates sample text and CSV files
- 📖 Reads text file content
- 📊 Reads and processes CSV data
- 📦 Moves and renames files automatically
- 📝 Creates log files for every operation
- ⚠️ Handles file-related exceptions gracefully
- 📋 Interactive menu-driven interface
- 🔄 Supports multiple operations in a single run

---

## 🛠️ Technologies Used

- Python 3
- os Module
- shutil Module
- csv Module
- logging Module
- datetime Module
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
automation-file/
│── main.py
│── logs/
│    └── log_YYYYMMDD_HHMMSS.log
│── file_demo/
│    ├── sample.txt
│    ├── archived_sample.txt
│    └── data.csv
│── README.md
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Saurabh18-code/automation-file.git
```

### 2. Open the Project Folder

```bash
cd automation-file
```

### 3. Run the Project

```bash
python main.py
```

---

## ▶️ How to Use

After running the program, you will see the following menu:

```
📁 FILE AUTOMATION DEMO

Menu:
1. Setup demo files
2. Run automation
3. Show files
4. Exit
```

### Option 1 – Setup Demo Files

- Creates a new directory
- Generates `sample.txt`
- Generates `data.csv`

### Option 2 – Run Automation

- Reads the text file
- Moves and renames the file
- Reads CSV records
- Stores all activities in log files

### Option 3 – Show Files

Displays all files inside the selected directory.

### Option 4 – Exit

Closes the application.

---

## 💻 Sample Output

```
📁 FILE AUTOMATION DEMO

Menu:
1. Setup demo files
2. Run automation
3. Show files
4. Exit

Enter choice: 1

Created directory: file_demo
✅ Sample files created
```

```
Enter choice: 2

--- Reading File ---
Hello, this is a sample text file for automation demo.

--- Moving File ---
File moved successfully

--- Reading CSV ---
Task_A - Completed
Task_B - Pending

✅ Operation completed
```

---

## 📚 Python Concepts Used

- File Handling
- Directory Management
- CSV File Processing
- Logging
- Exception Handling
- Functions
- Loops
- Conditional Statements
- Modules and Packages

---

## 🚀 Future Enhancements

- Graphical User Interface (Tkinter)
- File Compression (ZIP)
- Automatic File Backup
- Scheduled Automation
- Email Notifications
- PDF and Excel Report Generation
- Support for Multiple File Formats
- Real-Time Folder Monitoring

---

## 🎯 Learning Outcomes

This project helps in understanding:

- Python File Handling
- Automation using Python
- CSV Data Processing
- Logging Mechanism
- Error Handling
- Directory Operations
- Code Organization and Modularity

---

## 👨‍💻 Author

**Saurabh Vanjari**

GitHub: https://github.com/Saurabh18-code

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
