# File Integrity Checker using Docker and GitHub Actions

A beginner-friendly cybersecurity project that monitors a specific file for unauthorized changes using SHA256 hashing. The project is fully containerized with Docker and uses GitHub Actions for CI/CD automation.

## 🌟 Project Overview

This project ensures the integrity of a file named `important.txt`. It works by:
1. Generating a SHA256 hash of the file.
2. Storing it in `original_hash.txt`.
3. Comparing the current file hash against the original hash every time the script runs.
4. Outputting **"Integrity maintained"** if they match, or **"WARNING: Integrity mismatch detected"** if they don't.

Whenever code is pushed to GitHub, a GitHub Actions workflow automatically builds a Docker container and runs this check!

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3 installed
- Docker installed (optional, but recommended for testing the containerized version)

### Option 1: Run with Python
1. Clone this repository or navigate to the project directory.
2. Open a terminal and run the script:
   ```bash
   python checker.py
   ```
3. Modify `important.txt` (add a space, change a word).
4. Run the script again to see the warning:
   ```bash
   python checker.py
   ```
   *Note: If you want to reset the hash, delete `original_hash.txt` and run the script again.*

### Option 2: Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t integrity-checker .
   ```
2. Run the Docker container:
   ```bash
   docker run integrity-checker
   ```

---

## 🛠️ GitHub Actions Setup

This project includes a CI/CD pipeline that runs automatically.

1. Create a new repository on GitHub.
2. Push these project files to your GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```
3. Go to your repository on GitHub and click on the **Actions** tab.
4. You will see the `File Integrity Check CI` workflow running automatically. 
5. Click on the workflow run, then click on the `integrity-check` job to see the logs. The final step "Run Integrity Checker" will show whether the integrity was maintained!

### Sample CI/CD Workflow (`.github/workflows/ci.yml`)
```yaml
name: File Integrity Check CI
on: [push]
jobs:
  integrity-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Build Docker Image
        run: docker build -t integrity-checker .
      - name: Run Integrity Checker
        run: docker run integrity-checker
```

---

## 🎓 Viva / Presentation Guide

If you are presenting this project, here is a simple explanation of how it works:

**What is this project?**
This is a File Integrity Monitoring (FIM) tool. In cybersecurity, FIM is a technique used to check if sensitive files have been tampered with by malware or unauthorized users.

**How does it work?**
1. **Hashing:** We use Python's `hashlib` to calculate a mathematical representation (SHA256 hash) of our file. Even changing a single letter completely changes the hash.
2. **Verification:** We store the original hash. When the script runs, it generates a new hash of the current file and compares it to the original. If they differ, the file was modified!
3. **Containerization:** We use Docker to package the script and its environment. This ensures the script runs the exact same way on any computer.
4. **Automation:** We use GitHub Actions (CI/CD). Every time a change is pushed to the repository, GitHub automatically builds the Docker container and runs the integrity check. 

**Why is this important?**
It demonstrates the CIA Triad in cybersecurity, specifically **Integrity**. It proves that the data has not been altered in an unauthorized manner.

---

*Note: Line endings (CRLF vs LF) can change file hashes. If you get a mismatch on your very first run locally, simply delete `original_hash.txt` and run `python checker.py` once to generate a fresh hash for your specific system before pushing to GitHub!*
