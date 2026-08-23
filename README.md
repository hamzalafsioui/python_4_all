# 🧠 Python Mastery for AI Engineering

> **A comprehensive, hands-on curriculum built to take you from Python basics to software engineering and core mathematics for AI.**

This repository is a self-contained, practical learning suite designed for developers, data scientists, and aspiring AI engineers. Every module emphasizes practical execution: **learn, see, practice, and build**.

> 🚧 **Project Status:** **In Progress** (Modules `00` through `15` currently implemented)

---

## 🎯 Core Philosophy

**Build things. Break things. Fix things. Ship things.**

Every module in this repository follows a consistent, production-oriented structure:

1. **Learn** concepts with detailed explanations ([`theory.md`](./00_foundations/variables_and_types/theory.md))
2. **See** clean, runnable code demonstrations ([`examples.py`](./00_foundations/variables_and_types/examples.py))
3. **Practice** hands-on problems with solution validation ([`exercises.py`](./00_foundations/variables_and_types/exercises.py))
4. **Build** functional mini-projects ([`project.py`](./00_foundations/variables_and_types/project.py))
5. **Explore** interactively with data/math plots ([`notebook.ipynb`](./15_math_for_ai/linear_algebra_basics/notebook.ipynb) | *Data & Math modules*)

---

## 📂 Standard Module Folder Structure

```
module_folder/
├── README.md              # Module context, prerequisites, estimated time, and objectives
├── requirements.txt       # Python dependencies required for the module
└── topic_subfolder/
    ├── theory.md          # Theoretical foundations & best practices
    ├── examples.py        # Runnable code demonstrations
    ├── exercises.py       # Guided practice problems & answers
    ├── project.py         # Real-world mini-project implementation
    └── notebook.ipynb     # (Data & Math modules) Interactive visual Jupyter notebooks
```

---

## 🗺️ Currently Available Curriculum & Modules

### Phase 1: Python Foundations (`00`–`05`)
Master fundamental syntax, memory model, data structures, and program flow.

| Module | Subtopics Included | Primary Mini-Projects |
| :--- | :--- | :--- |
| 🔹 [`00_foundations`](./00_foundations) | Variables, primitive types, arithmetic/logical operators, I/O, PEP8 style | Interactive CLI Calculator |
| 🔹 [`01_control_flow`](./01_control_flow) | `if/else`, `match/case`, `for` & `while` loops, `break`/`continue`/`pass` | Number Guessing Game |
| 🔹 [`02_data_structures`](./02_data_structures) | Lists, tuples, sets, dictionaries, list/dict comprehensions | Contact Management System |
| 🔹 [`03_functions`](./03_functions) | Functions, positional/keyword arguments, `*args`/`**kwargs`, lambdas, recursion | Math Utility Library |
| 🔹 [`04_modules_packages`](./04_modules_packages) | Module importing, custom packages, `__init__.py`, virtual environments | Custom Python Package |
| 🔹 [`05_error_handling`](./05_error_handling) | `try/except`, `finally/else`, exception hierarchy, custom exceptions | Robust File Processor |

---

### Phase 2: Practical Python (`06`–`09`)
Work with file formats, object-oriented architecture, advanced language features, and Python's standard library.

| Module | Subtopics Included | Primary Mini-Projects |
| :--- | :--- | :--- |
| 🔹 [`06_file_handling`](./06_file_handling) | Reading/writing text files, JSON serialization, CSV manipulation | Data Format Converter Tool |
| 🔹 [`07_object_oriented_programming`](./07_object_oriented_programming) | Classes, objects, attributes, inheritance, polymorphism, encapsulation, magic methods | Bank Account Management System |
| 🔹 [`08_advanced_python`](./08_advanced_python) | Decorators, generators, iterators, closures, custom context managers | Reusable Context Manager |
| 🔹 [`09_standard_library`](./09_standard_library) | `os`/`sys`, `datetime`, `collections`, `itertools`, `argparse` | Automated CLI File Organizer |

---

### Phase 3: Software Engineering (`10`–`13`)
Build maintainable, well-tested, high-performance, and network-connected applications.

| Module | Subtopics Included | Primary Mini-Projects |
| :--- | :--- | :--- |
| 🔹 [`10_testing_debugging`](./10_testing_debugging) | `unittest`, `pytest`, interactive debugging with `pdb`, standard `logging` | Automated Test Suite & Log Audit |
| 🔹 [`11_performance_optimization`](./11_performance_optimization) | Time complexity (Big-O), code profiling, `threading`, `multiprocessing`, `asyncio` | Concurrent Web Scraper |
| 🔹 [`12_databases`](./12_databases) | SQLite basics, PostgreSQL connection, ORM with SQLAlchemy | Task Manager with DB Persistence |
| 🔹 [`13_networking_web_basics`](./13_networking_web_basics) | Sockets, HTTP requests, web scraping, REST APIs with Flask & FastAPI | Secure REST API & Web Scraper |

---

### Phase 4: Data & Math for AI (`14`–`15`)
The mathematical and data engineering foundation powering modern Artificial Intelligence.

| Module | Subtopics Included | Primary Mini-Projects |
| :--- | :--- | :--- |
| 🔹 [`14_data_science_basics`](./14_data_science_basics) | NumPy arrays, Pandas DataFrames/Series, data cleaning, Matplotlib & Seaborn visualization | Real-World Dataset EDA |
| 🔹 [`15_math_for_ai`](./15_math_for_ai) | Vectors, matrices, dot products, norms, Cosine similarity, Bayes' Theorem, Gaussian stats, Z-scores, CLT, Markov chains | Movie Recommender, Neural Layer Pass, Spam Classifier & Anomaly Detector |

---

## ⚡ Quick Start & Usage Guide

### 1. Prerequisites
- **Python 3.10** or higher.
- Git, VS Code, or any preferred IDE with Jupyter support.

### 2. Setup Environment
```bash
# Clone the repository
git clone https://github.com/hamzalafsioui/python_4_all.git
cd python_4_all

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate
```

### 3. Install Module Dependencies
Each module specifies its requirements in its root directory. For example, to install dependencies for **Module 15 (Math for AI)**:
```bash
pip install -r 15_math_for_ai/requirements.txt
```

### 4. Running Examples, Exercises & Projects
You can run any `.py` file directly from the command line:

```bash
# Run code demonstrations
python 00_foundations/variables_and_types/examples.py

# Run practice exercises
python 00_foundations/variables_and_types/exercises.py

# Run mini-projects
python 15_math_for_ai/linear_algebra_basics/project.py
```

### 5. Interactive Jupyter Notebooks
Modules 14 and 15 feature interactive `.ipynb` notebooks for visual plots and mathematical exploration. Launch Jupyter Notebook or JupyterLab:

```bash
jupyter notebook 15_math_for_ai/linear_algebra_basics/notebook.ipynb
```

---

## 📊 Completed Modules Summary

- [x] `00_foundations` | Python Foundations
- [x] `01_control_flow` | Decisions & Loops
- [x] `02_data_structures` | Lists, Tuples, Sets, Dicts
- [x] `03_functions` | Functions, Lambdas, Recursion
- [x] `04_modules_packages` | Packages & Environments
- [x] `05_error_handling` | Exceptions & Resilience
- [x] `06_file_handling` | File I/O, JSON, CSV
- [x] `07_object_oriented_programming` | OOP & Magic Methods
- [x] `08_advanced_python` | Decorators, Generators & Context Managers
- [x] `09_standard_library` | Standard Utilities & CLI
- [x] `10_testing_debugging` | Unit Testing & Logging
- [x] `11_performance_optimization` | Async, Multiprocessing & Profiling
- [x] `12_databases` | SQL & SQLAlchemy ORM
- [x] `13_networking_web_basics` | HTTP, FastAPI & Web Scraping
- [x] `14_data_science_basics` | NumPy, Pandas & Data Visualization
- [x] `15_math_for_ai` | Linear Algebra, Probability, Statistics & Matrix Computing

---

## 🤝 License & Contributions

This repository is maintained as an open-source learning resource. Contributions, fixes, and improvements are welcome!
