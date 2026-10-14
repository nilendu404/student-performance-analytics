# Student Performance Analytics System

**Course:** Python with AI — EWB Courses  
**Student:** NILENDU BARMAN  
**Submission deadline:** 15 October 2026

## Overview

A beginner-friendly Python data-analysis project that reads student marks and attendance from a CSV file, calculates student results, and reports class and subject performance. It uses Python functions, loops, conditions, NumPy, and Pandas. It does not use machine learning.

## Files

- `main.py` — loads, processes, and analyzes the dataset, then prints readable reports.
- `students.csv` — 20 fictional student records across four subjects and three departments.
- `Project_Documentation.md` — project write-up with the requested sections.
- `requirements.txt` — Python package dependencies.

## Requirements and run instructions

Use Python 3.9 or newer. From this folder, install the packages and run the program:

```bash
python -m pip install -r requirements.txt
python main.py
```

The script reads `students.csv` from the same folder. No file path changes are needed when the project folder is moved.

## Dataset

The CSV contains `Student_ID`, `Name`, `Department`, marks for Mathematics, Python, Artificial Intelligence, and English, plus `Attendance_Percentage`. Marks and attendance are percentages from 0 to 100. All names and records are fictional and created for this assignment.

## Calculation rules

- **Total marks:** sum of the four subject marks (maximum 400).
- **Average marks:** total divided by four subjects.
- **Grade:** A+ = 90–100, A = 80–89.99, B = 70–79.99, C = 60–69.99, D = 50–59.99, E = 40–49.99, F = below 40.
- **Pass:** at least 40 in every subject and attendance of at least 75%.
- **Fail:** below 40 in any subject or attendance below 75%.
- **Top performers:** the three highest average marks; ties are ordered by name.

## Analysis included

The output shows a preview of the data, each student's total, average, grade and pass/fail result, class average, pass/fail counts, highest and lowest student averages, the top three performers, and each subject's average/high/low mark and best average subject.