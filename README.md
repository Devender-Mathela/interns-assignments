# IgnitersHub Internship Assignments

Repository containing solutions for the Igniters Hub Python internship coding challenges.

---

## 📂 Project Structure

```
.
├── Challenge-1-Approximate-Search/
│   ├── main.py              # Approximate Search / Arithmetic Solver implementation
│   ├── input.txt            # Input test data
│   └── output.txt           # Generated solution output
│
├── Challenge-2-Arithmetic-Solver/
│   ├── main.py              # Implementation script
│   ├── words.txt            # Dictionary wordlist
│   └── words.py             # Wordlist backup
│
├── Challenge-3-Send-Email/
│   ├── main.py              # Automated SMTP email sender with attachment
│   ├── Professional.jpeg    # Required image attachment
│   └── README.md            # Detailed setup and instructions for Challenge 3
│
├── Challenge-4-Palindrome/
│   └── main.py              # Two-pointer palindrome validator
│
├── LICENSE
└── README.md
```

---

## 🚀 Challenges Overview

### 1. Challenge 1 – Approximate Search (Fuzzy Search)
- **Objective**: Given a dictionary of $N$ strings and an input query, find the top $k$ similar strings.
- **Technique**: Dynamic Programming (Levenshtein Distance) combined with subsequence and prefix matching.
- **Example**:
  - `Input >> abslutly` $\rightarrow$ `Output >> absolutely`
  - `Input >> actv` $\rightarrow$ `Output >> active, activist, activity`

### 2. Challenge 2 – Arithmetic Expression Evaluator
- **Objective**: Parse and evaluate mathematical expressions containing nested parentheses, brackets, exponents, and standard arithmetic operators from `input.txt` and write answers to `output.txt`.
- **Allowed Operators**: `+`, `-`, `*`, `/`, `^`, `()`, `[]`, `{}`.

### 3. Challenge 3 – Automated Email Sender with Attachment
- **Objective**: Programmatically construct and send an email to `hr@ignitershub.com` with student details and a professional photo attached.
- **Tech Stack**: Python standard library (`smtplib`, `email.message.EmailMessage`, `pathlib`).

### 4. Challenge 4 – Palindrome Checker
- **Objective**: Validate whether a given string is a palindrome.
- **Technique**: Two-pointer algorithm achieving $O(n)$ time complexity and $O(1)$ auxiliary space.

---

## 💻 General Requirements

- **Language**: Python 3.8+
- **External Dependencies**: None (all solutions rely strictly on Python's built-in standard library).

---

## 👤 Author

- **Name**: Devender Mathela
- **Semester**: 7th Semester
- **Branch**: Computer Science and Engineering
- **Roll Number**: 230180101017
