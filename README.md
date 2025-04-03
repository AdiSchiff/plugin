# plugin - Python Assignment

## Overview
This project is a Python-based API plugin that interacts with the **DummyJSON API**. It performs the following tasks:
1. **Connectivity Test** - Logs in using an API and verifies authentication.
2. **Evidence Collection** - Retrieves user details, posts, and comments.
3. **Structured & Reusable Code** - Ensures modularity and proper error handling.

## Setup & Installation
### 1️ Install Python dependencies
Ensure you have Python installed. If not, download it from [python.org](https://www.python.org/downloads/).

Then, install the required package:
```bash
pip install requests
```

### 2️ Clone the repository
```bash
git clone https://github.com/AdiSchiff/plugin.git
cd plugin
```

### 3️ Run the script
```bash
python main.py
```

## Features
### 1. User Authentication
- Logs in using predefined credentials.
- Retrieves an authentication token.

### 2. Data Retrieval
- **E1:** Fetches user details.
- **E2:** Retrieves 60 posts.
- **E3:** Fetches posts with associated comments.

### 3. Error Handling
- Manages authentication errors.
- Handles failed API responses gracefully.