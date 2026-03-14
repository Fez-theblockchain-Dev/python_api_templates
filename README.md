# python_api_templates

## 📝 Introduction

`python_api_templates` is a practical collection of REST API implementations using different Python technologies. This project demonstrates how to create, read, update, and delete (CRUD) JSON-based data using various frameworks and techniques. Whether you're a beginner exploring API development or an experienced developer seeking quick references, this repository offers clean, minimal templates in:

- Flask
- FastAPI
- Vanilla Python (no frameworks)

Each implementation is self-contained and easy to run, making it perfect for learning, prototyping, or comparing styles and performance.

---

## 📚 Table of Contents

- [Introduction](#-introduction)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Dependencies](#-dependencies)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributors](#-contributors)
- [License](#-license)

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/python_api_templates.git
cd python_api_templates
```

Install dependencies (for Flask and FastAPI examples):

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Flask API

```bash
python flask_api.py
```

Navigate to `http://127.0.0.1:5000` in your browser or use tools like Postman or `curl` to test.

---

### 2. FastAPI

```bash
uvicorn fastapi_api:app --reload
```

Visit the interactive docs at `http://127.0.0.1:8000/docs`.

---

### 3. Vanilla Python API

```bash
python vanilla_api.py
```

This runs a simple HTTP server on a basic port (e.g., 8080) with JSON file-based routing.

---

## 🗂️ Project Structure

```
python_api_templates/
│
├── flask_api.py         # Flask implementation
├── fastapi_api.py       # FastAPI implementation
├── vanilla_api.py       # Vanilla Python3 implementation
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

---

## ✨ Features

- Full CRUD support (Create, Read, Update, Delete)
- JSON-based data persistence (in-memory or basic file-based)
- Minimal setup for each framework
- Clean and well-documented code
- Easily extendable for your own projects

---

## 📦 Dependencies

Install all dependencies with:

```bash
pip install -r requirements.txt
```

Dependencies include:

- `Flask`
- `FastAPI`
- `uvicorn`

The Vanilla Python version does not require any third-party packages.
