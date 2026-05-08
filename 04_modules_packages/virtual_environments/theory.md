# Virtual Environments (`venv`)

A **Virtual Environment** is a tool that helps to keep the dependencies required by different projects separate by creating isolated python virtual environments for them.

---

## 1. Why do we need them?
Imagine Project A needs `Requests 1.0` but Project B needs `Requests 2.0`. If you install them globally, one will overwrite the other. 
- **Isolation**: Each project has its own library folder.
- **Cleanliness**: Your global Python installation stays clean.
- **Reproducibility**: You can export a list of requirements for others to use.

---

## 2. How to use `venv` (The Workflow)

### Step 1: Create the Environment
Run this in your project folder:
```bash
python -m venv .venv
```
*(This creates a folder named `.venv` containing a copy of the Python interpreter)*

### Step 2: Activate it
- **Windows**: `.venv\Scripts\activate`
- **Mac/Linux**: `source .venv/bin/activate`

Once activated, your terminal prompt will usually show `(.venv)`.

### Step 3: Install Packages
```bash
pip install requests
```

### Step 4: Deactivate
When done, just type:
```bash
deactivate
```

---

## 3. Managing Requirements
To share your project, you should tell others which libraries you used.
- **Export**: `pip freeze > requirements.txt`
- **Install from file**: `pip install -r requirements.txt`

---

> [!CAUTION]
> Never upload your `.venv` folder to GitHub. It's huge and system-specific. Instead, add `.venv/` to your `.gitignore` and only upload the `requirements.txt` file.
