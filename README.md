```markdown
# Homework: Working with Files and a Modular System

This repository contains implementations for four tasks in Python:

1. Task 1 — total_salary(path): compute total and average salaries from a CSV-like text file.
2. Task 2 — get_cats_info(path): parse a cats info file into a list of dictionaries.
3. Task 3 — hw03.py: a directory tree viewer that prints directories and files in different colors.
4. Task 4 — assistant.py: a simple CLI assistant for basic contact management.

Setup
1. Create a virtual environment and activate it:

   python -m venv .venv
   # On macOS / Linux:
   source .venv/bin/activate
   # On Windows (PowerShell):
   .venv\Scripts\Activate.ps1

2. Install dependencies:

   pip install -r requirements.txt

Files
- total_salary.py — Task 1 (function `total_salary(path)`)
- cats_info.py — Task 2 (function `get_cats_info(path)`)
- hw03.py — Task 3 (directory tree viewer; run with a directory path argument)
- assistant.py — Task 4 (CLI assistant; run without arguments)
- requirements.txt — dependency list (colorama)

Usage examples

Task 1 (total salary):
```python
from total_salary import total_salary
total, average = total_salary("data/salaries.txt")
print(f"Total salary: {total}, Average salary: {average}")
```

Task 2 (cats info):
```python
from cats_info import get_cats_info
cats = get_cats_info("data/cats.txt")
print(cats)
```

Task 3 (directory tree):
```bash
python hw03.py /path/to/directory
```

Task 4 (assistant CLI):
```bash
python assistant.py
```
Commands supported by assistant: hello, add, change, phone, all, close, exit

Notes
- The modules handle common file-related errors gracefully by logging warnings or errors and returning reasonable defaults.
- hw03.py uses colorama to color directory vs file names. Ensure the virtual environment has colorama installed.
