# Project Documentation

## 1. Name

**Project title:** Student Performance Analytics System  
**Student name:** NILENDU BARMAN  
**Course:** Python with AI — EWB Courses  

## 2. Overview

The Student Performance Analytics System is a Python program that organizes student marks and attendance from a CSV dataset and turns them into a clear performance report. It presents individual student results, class-level statistics, subject comparisons, and the top performers. The project demonstrates foundational Python data analysis and does not use advanced machine learning.

## 3. Objective

The objective is to make it easier to understand student and class performance without calculating each result by hand. The program calculates totals and averages, assigns grades, applies a pass/fail rule, and highlights patterns such as the strongest subject and highest-performing students.

## 4. Implementation

### Dataset and loading

The project uses `students.csv`, containing 20 fictional student records. Each record has a student ID, name, department, marks in Mathematics, Python, Artificial Intelligence, and English, and an attendance percentage. Pandas `read_csv()` loads the records into a DataFrame. The program checks that the required columns are available before analysis.

### Processing and calculation

Reusable functions divide the work into loading data, assigning a grade, processing student records, and displaying summaries. NumPy converts subject marks to a numerical array and calculates row totals, averages, and subject statistics. Pandas is used to organize the data, sort the top performers, and calculate subject averages.

A loop processes student records and assigns a grade and result using conditions. The grading rule is A+ for an average of at least 90, A for at least 80, B for at least 70, C for at least 60, D for at least 50, E for at least 40, and F for below 40. A student passes when every subject mark is at least 40 and attendance is at least 75%; otherwise the student fails.

### Analysis and output

The program prints a data preview and a student-wise summary, followed by the overall class average, pass/fail counts, highest and lowest average, and the top three performers. It also reports each subject's average, highest mark, lowest mark, and identifies the subject with the best class average. Ties among the top performers are ordered alphabetically by name.

### How to run

Install the packages listed in `requirements.txt`, then run `python main.py` from the project folder. The program reads `students.csv` located beside `main.py`.

## 5. Final Outcome

The completed project produces a readable analytics report from the included student dataset. It automates individual and class calculations, applies stated grading and attendance rules consistently, and makes subject performance and top students easy to identify.