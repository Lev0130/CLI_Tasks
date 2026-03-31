# 📝 CLI Task Manager

A simple command-line task manager built with Python.
This project helps you create, track, and update your daily tasks directly from the terminal using a lightweight JSON-based storage system.

---

## 🚀 Features

* ➕ Add new tasks
* 📋 View tasks grouped by date
* ✅ Mark tasks as completed
* 💾 Persistent storage using a JSON file
* 🧠 Simple and readable structure

---

## 🛠️ How It Works

This tool uses Python’s built-in `argparse` module to handle command-line arguments and `json` to store tasks locally.

Each task includes:

* An ID
* A date
* A description
* A status (`pending` or `done`)

All data is stored in a `data.json` file.

---

## 📦 Usage

Run the script from the terminal:

```bash
python file.py <command> [arguments]
```

---

### ➕ Add a task

```bash
python file.py add "Buy groceries"
```

---

### 📋 List all tasks

```bash
python file.py list
```

Tasks are grouped by date and displayed in a readable format.

---

### ✅ Mark a task as done

```bash
python file.py done 1
```

Where `1` is the task ID.

---

## 📁 Project Structure

```
.
├── file.py
├── data.json
└── README.md
```

---

## 💡 Design Notes

* Tasks are stored in a JSON file for simplicity and portability.
* The CLI is built using subcommands (`add`, `list`, `done`) for a clean user experience.
* The project focuses on clarity and fundamental backend concepts rather than frameworks.

---

## 🧠 What I Learned

* Working with JSON data in Python
* Handling command-line arguments using `argparse`
* Structuring a small CLI application
* Managing state through file persistence
* Debugging and reasoning through data transformations

---

## 🔮 Possible Improvements

* Edit and delete tasks
* Add deadlines or priorities
* Filter tasks by status or date
* Improve formatting and UI in the terminal
* Replace JSON storage with a database

---

## 📌 Notes

This project was built as a learning exercise to strengthen my understanding of Python, data handling, and command-line tools.

---

## 👤 Author

Leo
