# Working with CSV in Python

**CSV** (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. Each line of the file is a data record, and each record consists of one or more fields, separated by commas.

---

## 1. The `csv` Module
Python includes a built-in `csv` module to handle the complexities of CSV files (like commas inside values).

```python
import csv
```

---

## 2. Reading CSV Files
There are two main ways to read a CSV:

### A. Using `csv.reader` (List-based)
Each row is returned as a **list** of strings.
```python
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # row[0], row[1], etc.
```

### B. Using `csv.DictReader` (Dictionary-based)
Each row is returned as a **dictionary**, where the keys are the column headers. **(Highly Recommended)**
```python
with open('data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'], row['Age'])
```

---

## 3. Writing CSV Files
Similarly, there are two ways to write:

### A. Using `csv.writer`
```python
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Hamza", "25"])
```

### B. Using `csv.DictWriter`
```python
with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Hamza', 'Age': '25'})
```

---

> [!IMPORTANT]
> When opening a file for writing CSVs, always include `newline=''` in the `open()` function. This prevents extra blank lines from being added on some operating systems (like Windows).

---

## Resources

- **Official Python csv Module Documentation** – https://docs.python.org/3/library/csv.html
- **Real Python: Working with CSV Files** – https://realpython.com/python-csv/
- **Corey Schafer: CSV Files in Python (YouTube)** – https://www.youtube.com/watch?v=9U3jS-SRVo4
- **GeeksforGeeks: CSV File Reading and Writing in Python** – https://www.geeksforgeeks.org/python-csv-module/
- **Python for Data Analysis (Book) – Chapter on CSV I/O** – https://www.oreilly.com/library/view/python-for-data/9781491957653/
